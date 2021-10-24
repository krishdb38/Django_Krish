from django.db import models

# Create your models here.
class Product(models.Model) :
    name = models.CharField(max_length = 50, verbose_name= "Product Name ")
    price = models.IntegerField(verbose_name= "Price of Product ")
    description = models.TextField(verbose_name="Product Detail")
    stock = models.IntegerField(verbose_name= "Stock" )
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="Product registered date")
    
    def __str__(self) :
        return self.name
    
    class Meta:
        db_table = "fastcampus_product"  # table Name
        verbose_name = "product"  # can write in local language
        verbose_name_plural = "products"
    
