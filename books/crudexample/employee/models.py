from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=50)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField(max_length=40)
    econtact = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'employee'