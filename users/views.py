from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views import View
from users.forms import CompanySignupForm
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = CompanySignupForm
    success_url = reverse_lazy("gratify:home")

    def form_valid(self, form):
        # Create the user.
        user = form.save(commit=False)
        user.save()
        # Create the Company using the company_name field.
        company_name = form.cleaned_data.get("company_name")
        # Company.objects.create(name=company_name, owner=user)
        login(self.request, user)
        return super().form_valid(form)



class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("gratify:home")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy("users:login"))
