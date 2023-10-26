from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PhotoUploadForms(forms.Form):
    photo = forms.ImageField()
class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    password =  forms.CharField(label="Password", widget=forms.PasswordInput)

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

