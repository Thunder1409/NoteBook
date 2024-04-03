from django import forms
from django.forms import ClearableFileInput
from .models import UserData


# replace in_input with form input fields css class

class Create_Account_Form(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

# Form to create accounts
class Login_Form(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

