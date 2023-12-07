from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    ItemViewSet,
    ItemCategoryViewSet,
    OrderItemList, OrderItemDetail,
    OrderList, OrderDetail, )

app_name = 'core'

router = SimpleRouter()
router.register('items', ItemViewSet, basename='items')
router.register('categories', ItemCategoryViewSet, basename='categories')

urlpatterns = [
    path('order_items/', OrderItemList.as_view(), name='order_item_list'),
    path('order_items/<int:pk>/', OrderItemDetail.as_view(), name='order_item_detail'),
    path('order/', OrderList.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
]

urlpatterns += router.urls