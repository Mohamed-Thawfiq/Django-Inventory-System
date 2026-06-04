from django.db import models
from inventory.models import *
# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=100)
    since=models.DateField(null=True)

    def __str__(self):
        return self.name
    
class orders(models.Model):
    customer_ref=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    product_ref=models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    order_num=models.CharField(max_length=20,null=True)
    order_date=models.DateField(null=True)
    quantity=models.FloatField(default=0)
    amount=models.FloatField(default=0)
    gst_amount=models.FloatField(default=0)
    bill_amount=models.FloatField(default=0)

    def __str__(self):
    
        return self.order_num
    