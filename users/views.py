from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views import View
from gratify.models import EmployeeInvite
from users.forms import EmailAuthenticationForm, EmployeeSignupForm, EmployerSignupForm
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.shortcuts import render


class EmployerSignupView(FormView):
    """Handles employer registration and company creation."""
    template_name = "users/employer_signup.html"
    form_class = EmployerSignupForm
    success_url = reverse_lazy("gratify:home")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = form.cleaned_data.get("username")
        user.save()
        return super().form_valid(form)


class EmployeeSignupView(FormView):
    """Handles employee registration via invite link."""
    template_name = "users/employee_signup.html"
    form_class = EmployeeSignupForm
    success_url = reverse_lazy("gratify:home")

    def dispatch(self, request, *args, **kwargs):
        try:
            self.invite = EmployeeInvite.objects.get(token=self.kwargs["token"], used=False)
        except EmployeeInvite.DoesNotExist:
            return render(
                request,
                "users/employee_invite_error.html",
                {
                    "message": "It seems like this invite link has expired.\nContact your admin to get a new link."
                },
                status=400
            )

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

        self.invite.delete()

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
