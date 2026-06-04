
from django.urls import path
from .views import *
urlpatterns=[
    
    path('product/',product_page),
    path('product/view/',product_view),
    path('product/delete/<int:id>/',delete_product,name='product_delete'),
    path('product/update/<int:id>/',update_product,name='product_update'),
    
]