from django.urls import path
from build_people import views

app_name = "build_people"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("preview/", views.PreviewView.as_view(), name="preview"),
    path("subscriptions/", views.SubscriptionsView.as_view(), name="subscriptions"),
    path("core_values/", views.CoreValuesView.as_view(), name="core_values"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
