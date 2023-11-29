from django.urls import path
from .views import ItemList, ItemDetail

app_name = 'core'

urlpatterns = [
    path('items/', ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
]