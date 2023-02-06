from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    prince = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    published_data = models.DateTimeField()
    image = models.ImageField(upload_to="shop/images",default="")

    # myadim shop show product object 1 ,2 then chenge this
    def __str__(self):
        return self.product_name



