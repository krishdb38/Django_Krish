from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password , make_password

class RegistrationForms(forms.Form):
    email = forms.EmailField(error_messages={
        "required": "Input Email"
    },
    max_length=20, label = "Email")
    password = forms.CharField(max_length=100,
                               error_messages={
                                   "required": "Please Input Your Password"
                               },
                               widget=forms.PasswordInput, label="Password"
                               )
    re_password = forms.CharField(max_length=20,
                               error_messages={
                                   "required": "Please Input Your Password"
                               },
                               widget=forms.PasswordInput, label="Password confirm"
                               )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")
        
        if password and re_password:
            if password != re_password:
                self.add_error("password", "Password not match")
                self.add_error("re_password", "Password not match")
                
            else:
                fcuser = Fcuser(
                    email = email,
                    password = make_password(password)
                )
                fcuser.save()
                

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        "required": "Input Email"
    },
        max_length=20, label="Email")
    password = forms.CharField(max_length=100,
                               error_messages={
                                   "required": "Please Input Your Password"
                               },
                               widget=forms.PasswordInput, label="Password"
                               )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
        if email and password: 
            try :
                fcuser = Fcuser.objects.get(email =email )
            except Fcuser.DoesNotExist:
                self.add_error("username", "ID Does not exist")
                return
            
            if not check_password(password, fcuser.password):
                self.add_error("password" , "Password Do not match ")
            else:
                self.email = fcuser.email
            
