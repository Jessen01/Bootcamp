from django import  forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:      
        model = User
        fields = ['username', 'first_name', 'last_name','password', 'password2']

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
