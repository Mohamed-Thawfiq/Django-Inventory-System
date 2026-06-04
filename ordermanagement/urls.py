
from django.urls import path
from .views import *

urlpatterns = [
    path('all/customers/', customer_list),
    path('add/customer/', customer_add),
    path('delete/customer/<int:id>/', customer_delete, name='customer_delete'),
    path('update/customer/<int:id>/', customer_update, name='customer_update'),
    path('add/',orders_add),
    path('view_orders/',all_orders),
    path('deleted/<int:id>/',delete_orders,name='order_deleted'),
    path('updated/<int:id>/',update_orders,name='order_update')
]