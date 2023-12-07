from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets

from .models import Item, OrderItem, Order, ItemCategory
from .serializers import ItemSerializer, OrderSerializer, ItemCategorySerializer, OrderItemSerializer
from .permissions import IsOwnerOrReadOnly


# ITEMS
class ItemViewSet(viewsets.ModelViewSet):
    """
    Perform actions with items for authenticated users, read by all
    """
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# ITEM CATEGORY
class ItemCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve product categories
    """
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    permission_classes = (permissions.AllowAny,)


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
class OrderItemList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]      # should be only for owner
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


