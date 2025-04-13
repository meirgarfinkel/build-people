from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("signup/", views.EmployerSignupView.as_view(), name="employer_signup"),
    path("signup/<uuid:token>/", views.EmployeeSignupView.as_view(), name="employee_signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
