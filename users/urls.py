from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("employer_signup/", views.EmployerSignupView.as_view(), name="employer_signup"),
    path("employee_signup/<uuid:token>", views.EmployeeSignupView.as_view(), name="employee_signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
