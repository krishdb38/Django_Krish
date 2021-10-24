from django.db import models

# Create your models here.
class Order(models.Model):
    fcuser = models.ForeignKey("fcuser.Fcuser", on_delete=models.CASCADE, verbose_name="ordered by")
    product = models.ForeignKey('product.Product', on_delete= models.CASCADE , verbose_name= "product Ordered")
    quantity = models.IntegerField(verbose_name="Number of Product ordered")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="ordered date")
    
    def __str__(self):
        pass
        return str(self.fcuser) + "_" + self.product
        # foreign key need to change to string 
    
    
    class Meta:
        db_table = "fastcampus_order" # table Name
        verbose_name = "order" # can write in local language
        verbose_name_plural = "orderes"