from django.contrib import admin

from .models import Item, OrderItem, Order, ItemCategory


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'quantity')

    def item_id(self, obj):
        return obj.id


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'owner', 'item_name')

    def order_id(self, obj):
        return obj.order.id

    def item_name(self, obj):
        return obj.item.item_name


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'owner', 'created_at', 'status')

    def order_id(self, obj):
        return obj.id


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ItemCategory)
admin.site.register(Order, OrderAdmin)
