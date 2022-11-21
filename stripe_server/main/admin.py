from django.contrib import admin
from .models import Item, Order, Currency


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ['name', 'description', 'price']
    list_filter = ['name', 'price']


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created']


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Currency, CurrencyAdmin)
