from django.urls import path
from .views import (
    ItemList, ItemDetail,
    ItemCategoryList, ItemCategoryDetail,
    OrderItemList, OrderItemDetail,
    OrderList, OrderDetail, )

app_name = 'core'

urlpatterns = [
    path('items/', ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('category/', ItemCategoryList.as_view(), name='item_category_list'),
    path('category/<int:pk>/', ItemCategoryDetail.as_view(), name='item_detail'),
    path('order_items/', OrderItemList.as_view(), name='order_item_list'),
    path('order_items/<int:pk>/', OrderItemDetail.as_view(), name='order_item_detail'),
    path('order/', OrderList.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
]