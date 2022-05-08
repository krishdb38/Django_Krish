import imp
from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import User

from profiles.utils import generate_account_number
# Create your models here.
class Profile(models.Model):
    """
    Class for the owner of the invoice
    """
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    account_number = models.CharField(max_length= 26, blank=True )
    company_name = models.CharField(max_length=200, )
    company_info = models.TextField()
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now= True)
    #avatar = 
    #company_logo = 

    def __str__(self) -> str:
        return f"Profile  of the User : {self.user.username}"
    def save(self, *args, **kwargs):
        if self.account_number == '':
            self.account_number = generate_account_number()
        return super().save(*args, **kwargs)

    # def clean(self) -> None:
    #     if len(self.account_number) != 26:
    #         raise ValidationErr("Bank account must be 26 character")