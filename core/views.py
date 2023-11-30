from rest_framework import generics, permissions

from .models import Item, OrderItem, Order, ItemCategory
from .serializers import ItemSerializer, OrderSerializer, ItemCategorySerializer, OrderItemSerializer
from .permissions import IsOwnerOrReadOnly


# ITEMS
class ItemList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# ITEM CATEGORY
class ItemCategoryList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ItemCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


# ORDERS
class OrderList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ORDER ITEMS
class OrderItemList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


