from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from users.enums import Roles
from users.models import User
from django.utils.text import slugify


class EmployerSignupForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2", "company_name")

    def clean_username(self):
        # Skip the unique check for username as we've made it non-unique
        return self.cleaned_data.get("username", "")
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        cleaned_data["role"] = Roles.EMPLOYER

        if first_name and last_name:
            cleaned_data["username"] = slugify(f"{first_name} {last_name}")

        return cleaned_data


class EmployeeSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        """Set email as a hidden field and prevent changes."""
        super().__init__(*args, **kwargs)
        email = kwargs.get("initial", {}).get("email")
        self.fields["email"] = forms.EmailField(
            initial=email,
            widget=forms.HiddenInput(),
            label=""
        )
    
    def clean_email(self):
        """Ensure the email is not already registered."""
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name:
            cleaned_data["username"] = slugify(f"{first_name} {last_name}")

        return cleaned_data


class EmailAuthenticationForm(AuthenticationForm):
    """Login form using email instead of username."""
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"autofocus": True}))


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
    
    def clean_email(self):
        """Ensure the email is not already registered."""
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name:
            cleaned_data["username"] = slugify(f"{first_name} {last_name}")

        return cleaned_data
