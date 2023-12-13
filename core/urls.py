from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    ItemViewSet,
    ItemCategoryViewSet,
    OrderItemViewSet,
    OrderList, OrderDetail, )

app_name = 'core'

router = SimpleRouter()
router.register('items', ItemViewSet, basename='items')
router.register('categories', ItemCategoryViewSet, basename='categories')
router.register(r'^(?P<order_id>\d+)/order_items', OrderItemViewSet, basename='order_items')

urlpatterns = [
    path('order/', OrderList.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
]

urlpatterns += router.urls