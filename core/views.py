from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from django.core.exceptions import ValidationError

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
        if self.request.user.is_staff:
            return res
        user = self.request.user
        return res.filter(owner=user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner, ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ORDER ITEMS
class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner, ]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self, *args, **kwargs):
        res = super().get_queryset()
        order_id = self.kwargs.get("order_id")
        user = self.request.user
        if user.is_staff:
            return res.filter(order__id=order_id)
        return res.filter(order__id=order_id, owner=user)

    def perform_create(self, serializer):
        order = get_object_or_404(Order, id=self.kwargs.get("order_id"))
        serializer.save(order=order, owner=self.request.user)

    # TODO: update position if order_item in order
    # TODO: reserve items from stock until done or cancelled
    # TODO: change get_or_404 to get_or_create for new orders