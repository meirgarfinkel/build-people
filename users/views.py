from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views import View
from gratify.models import Company, EmployeeInvite
from users.forms import EmailAuthenticationForm, EmployeeSignupForm, EmployerSignupForm
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView

from users.models import User


class EmployerSignupView(FormView):
    """Handles employer registration and company creation."""
    template_name = "users/employer_signup.html"
    form_class = EmployerSignupForm
    success_url = reverse_lazy("gratify:home")

    def form_valid(self, form):
        # Create the user.
        user = form.save(commit=False)
        user.username = form.cleaned_data.get("username")
        user.role = form.cleaned_data.get("role")
        user.save()
        # Create the Company using the company_name field.
        company_name = form.cleaned_data.get("company_name")
        company = Company.objects.create(name=company_name, owner=user)
        user.company = company
        user.save()
        login(self.request, user)
        return super().form_valid(form)


class EmployeeSignupView(FormView):
    """Handles employee registration via invite link."""
    template_name = "users/employee_signup.html"
    form_class = EmployeeSignupForm
    success_url = reverse_lazy("gratify:home")

    def dispatch(self, request, *args, **kwargs):
        self.invite = get_object_or_404(EmployeeInvite, token=self.kwargs["token"], used=False)
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        """Pass invite email to form."""
        kwargs = super().get_form_kwargs()
        kwargs["initial"] = {"email": self.invite.email}
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = form.cleaned_data.get("username")
        user.company = self.invite.company
        user.save()

        self.invite.used = True
        self.invite.save()

        login(self.request, user)
        return super().form_valid(form)


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    authentication_form = EmailAuthenticationForm
    success_url = reverse_lazy("gratify:home")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy("users:login"))
