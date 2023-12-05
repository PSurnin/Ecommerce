from rest_framework import serializers
from core.models import Order, OrderItem, Item, ItemCategory


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    category = ItemCategorySerializer()

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        category = validated_data.pop("category")
        instance, created = ItemCategory.objects.get_or_create(**category)
        item = Item.objects.create(**validated_data, category=instance)

        return item

    # TODO: check out more thorough
    # TODO restrict ownership transfer?
    def update(self, instance, validated_data):
        if "category" in validated_data:
            nested_serializer = self.fields["category"]
            nested_instance = instance.category
            nested_data = validated_data.pop("category")
            nested_serializer.update(nested_instance, nested_data)

        return super(ItemSerializer, self).update(instance, validated_data)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    # def validate(self, validated_data):
    #     order_quantity = validated_data["quantity"]
    #     product_quantity = validated_data["product"].quantity
    #
    #     order_id = self.context["view"].kwargs.get("order_id")
    #     product = validated_data["product"]
    #     current_item = OrderItem.objects.filter(order__id=order_id, product=product)
    #
    #     if order_quantity > product_quantity:
    #         error = {"quantity": _("Ordered quantity is more than the stock.")}
    #         raise serializers.ValidationError(error)
    #
    #     if not self.instance and current_item.count() > 0:
    #         error = {"product": _("Product already exists in your order.")}
    #         raise serializers.ValidationError(error)
    #
    #     if self.context["request"].user == product.seller:
    #         error = _("Adding your own product to your order is not allowed")
    #         raise PermissionDenied(error)
    #
    #     return validated_data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
