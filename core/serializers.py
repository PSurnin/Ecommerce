from rest_framework import serializers
from core.models import Order, OrderItem, Item, ItemCategory


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True,)
    category = ItemCategorySerializer()

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        category = validated_data.pop("category")
        instance, _ = ItemCategory.objects.get_or_create(**category)
        item = Item.objects.create(**validated_data, category=instance)

        return item

    def update(self, instance, validated_data):
        if "category" in validated_data:
            nested_serializer = self.fields["category"]
            nested_instance = instance.category
            nested_data = validated_data.pop("category")
            nested_serializer.update(nested_instance, nested_data)

        return super(ItemSerializer, self).update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


# TODO: another serializer for item update view?
# In case of update orderItem only changes amount of ordered, nothing else
class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'item', 'quantity']

    def create(self, validated_data):
        order = validated_data.pop("order")
        instance, _ = Order.objects.get_or_create(**order)
        order_item = OrderItem.objects.create(**validated_data, order=instance)

        return order_item

    def validate(self, validated_data):
        order_quantity = validated_data['quantity']
        product_quantity = validated_data['item'].quantity

        if order_quantity > product_quantity:
            error = {"quantity": "Ordered quantity is more than the stock."}
            raise serializers.ValidationError(error)

        return validated_data

    # TODO: update for updated OrderItem amount
