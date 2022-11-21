from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('buy/<int:id>/', views.buy_item, name='buy'),
    path('buy_order/<int:id>/', views.buy_order, name='buy_order'),
    path('item/<int:id>/', views.item_info, name='item_info'),
    path('order/<int:id>/', views.order_info, name='order_info'),
    path('/checkout_cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('/checkout_success/', views.checkout_success, name='checkout_success')
]
