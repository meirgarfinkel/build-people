from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "gratify/home.html"


class PreviewView(LoginRequiredMixin, TemplateView):
    template_name = "gratify/preview.html"
