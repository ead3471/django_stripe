from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import stripe
import os
from dotenv import load_dotenv
from json import dumps

from .models import Item


load_dotenv()
STRIPE_SK = os.getenv('STRIPE_SECRET_KEY')
STRIPE_PK = os.getenv('STRIPE_PUBLIC_KEY')

stripe.api_key = STRIPE_SK


def create_product_if_not_exist(item: Item) -> stripe.Product:
    product = stripe.Product.retrieve(str(item.id))
    if not product:
        product = stripe.Product.create(id=item.pk, name=item.name)

    return product

def buy_item(request, id):
    item = Item.objects.get(pk=id)
    # product = create_product_if_not_exist(item)
    print(f"{request.build_absolute_uri('/')}/checkout_success/")

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                'price_data': {
                    'currency': item.currency.code,
                    'product_data': {
                    'name': item.name,
                    },
        'unit_amount': int(item.price*100),
      },
      'quantity': 1,
    },
            ],
            mode='payment',
            success_url=f"{request.build_absolute_uri('/')}/checkout_success/",
            cancel_url=f"{request.build_absolute_uri('/')}/checkout_cancel/",
        )
    except Exception as e:
        return HttpResponse(str(e))

    #print(dumps({"session": checkout_session}))
    return HttpResponse(dumps(checkout_session))


def item_info(request, id):
    item = Item.objects.get(pk=id)
    context = {
        "item": item,
        "stripe_pk": STRIPE_PK
    }
    return render(request, template_name='main/item_info.html', context=context)


def checkout_success(request):
    return redirect('/checkout_success/')


def checkout_cancel(request):
    return redirect('/checkout_cancel/')
