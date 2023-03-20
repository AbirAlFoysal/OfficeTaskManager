from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)
    designation = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'full_name', 'designation', 'password1', 'password2')
