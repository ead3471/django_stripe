from django.contrib import admin
from .models import Item, Order, Currency, Discount, Tax


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'currency']
    search_fields = ['name', 'description', 'price']
    list_filter = ['name', 'price']


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'discount', 'tax']


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percent_off', 'description', 'stripe_id']


class TaxAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tax_rate', 'description', 'stripe_id']


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)
