from django.urls import path
from gratify import views

app_name = "gratify"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("preview/", views.PreviewView.as_view(), name="preview"),
    path("subscriptions/", views.SubscriptionsView.as_view(), name="subscriptions"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
