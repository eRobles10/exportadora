from django.contrib import admin
from .models import Order, OrderStatus, Products, Border

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'author', 'quantity', 'product',
                    'border', 'orderStatus', 'created', 'updated')


class OrderStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class BorderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Order, OrderAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Border, BorderAdmin)
