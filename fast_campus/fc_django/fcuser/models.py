from django.db import models

# Create your models here.
class Fcuser(models.Model):
    email = models.EmailField(verbose_name= "Email Field ")
    password = models.CharField(max_length = 20, verbose_name= "Password Name ")
    register_date = models.DateTimeField(auto_now_add = True, verbose_name= "Registered Date ")
    
    def __str__(self):
        return self.email
        
        
    class Meta:
        db_table = "fastcampus_user"  # table Name
        verbose_name = "user"  # can write in local language
        verbose_name_plural = "users"
