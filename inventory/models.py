from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=200,null=False)
    product_description=models.CharField(max_length=1000,null=True)
    price=models.FloatField(default=0)
    tax=models.IntegerField(default=0)
    food_type=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name    