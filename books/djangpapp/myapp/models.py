from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'student' # name of Table
        
    
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=50)
    econtant = models.CharField(max_length=15)
    
    def __str__(self):
        return self.ename +"__" + self.econtant
    
    class Meta:
        db_table = 'employee'
