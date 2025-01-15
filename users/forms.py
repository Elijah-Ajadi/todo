from django.utils import timezone
from django import forms
from django.db import models
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    phone_number =forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match")
        return confirm_password

    def save(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        phone_number = self.cleaned_data.get("phone_number")
        user = User.objects.create_user(username=username, email=email, password=password, phone_number=phone_number)
        return user