from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)
    contactno = forms.IntegerField(widget=forms.NumberInput)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model= Profile
        fields= ['fullname', 'address', 'email' , 'contactno' , 'documents' ,'username' ,'password' ,'confirm_password']


