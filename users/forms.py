from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CompanySignupForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "company_name")
