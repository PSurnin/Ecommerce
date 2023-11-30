from rest_framework import generics

from .models import Item, OrderItem, Order
from .serializers import ItemSerializer
from .permissions import IsOwnerOrReadOnly


class ItemList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
