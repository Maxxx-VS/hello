from django import forms

class PhotoUploadForms(forms.Form):
    photo = forms.ImageField()