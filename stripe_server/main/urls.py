from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:id>/', views.buy_item, name='buy'),
    path('item/<int:id>/', views.item_info, name='item_info'),
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/<int:id>/', views.order_info, name='order_info'),
    path('orders/<int:id>/buy/', views.buy_order, name='buy_order'),
    path('checkout_cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('checkout_success/', views.checkout_success, name='checkout_success')
]
