from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets

from .models import Item, OrderItem, Order, ItemCategory
from .serializers import ItemSerializer, OrderSerializer, ItemCategorySerializer, OrderItemSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner


# ITEMS
class ItemViewSet(viewsets.ModelViewSet):
    """
    Perform actions with items for authenticated users, read by all
    """
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
    permission_classes = [IsOwner, ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        res = super().get_queryset()
        user = self.request.user
        return res.filter(owner=user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner, ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ORDER ITEMS
class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner,]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self, *args, **kwargs):
        res = super().get_queryset()
        order_id = self.kwargs.get("order_id")
        user = self.request.user
        return res.filter(order__id=order_id, owner=user)