from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Answer


class UserRegisterForm(UserCreationForm):
    "To Register User first Time "
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    " Update User after register "
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]


class ProfileUpdateForm(forms.ModelForm):
    "Update Profile of User "

    class Meta:
        model = Profile
        fields = [
            "image", 'bio', 'skills', 'aoi', 'github', 'linkedin'
        ]


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer_field']
