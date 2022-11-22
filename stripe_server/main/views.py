from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import stripe
import os
from dotenv import load_dotenv
from json import dumps

from .models import Item, Order


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
    item = get_object_or_404(Item, pk=id)

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

    return HttpResponse(dumps(checkout_session))


def buy_order(request, id):
    order = get_object_or_404(Order, pk=id)
    order_items = order.product.all()

    taxes = []
    if order.tax:
        if not order.tax.stripe_id:
            print('create tax')
            tax = stripe.TaxRate.create(display_name=order.tax.name,
                                        description=order.tax.description,
                                        percentage=order.tax.tax_rate,
                                        inclusive=False,)
            order.tax.stripe_id = tax.stripe_id
            order.tax.save()
        taxes.append(order.tax.stripe_id)

    line_items = [{
                    'price_data': {
                        'currency': item.currency.code,
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price*100),
                    },
                    'tax_rates': taxes,
                    'quantity': 1,
                }
                for item in order_items
    ]
    try:
        discounts = []
        if order.discount:
            if not order.discount.stripe_id:
                coupon = stripe.Coupon.create(
                    percent_off=order.discount.percent_off,
                    name=order.discount.name,
                    duration='once')
                order.discount.stripe_id = coupon.stripe_id
                order.discount.save()
            discounts.append({'coupon': order.discount.stripe_id})

        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=f"{request.build_absolute_uri('/')}/checkout_success/",
            cancel_url=f"{request.build_absolute_uri('/')}/checkout_cancel/",
            discounts=discounts
        )
    except Exception as e:
        return HttpResponse(str(e))

    return HttpResponse(dumps(checkout_session))


def item_info(request, id):
    import platform
    print(platform.python_version())
    item = get_object_or_404(Item, pk=id)
    context = {
        "item": item,
        "stripe_pk": STRIPE_PK
    }
    return render(request,
                  template_name='main/item_info.html',
                  context=context)


def order_info(request, id):
    order = get_object_or_404(Order, pk=id)
    context = {
        "order": order,
        "stripe_pk": STRIPE_PK
    }
    return render(request,
                  template_name='main/order_info.html',
                  context=context)


def checkout_success(request):
    return redirect('/checkout_success/')


def checkout_cancel(request):
    return redirect('/checkout_cancel/')

