from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from hx_requests.views import HtmxViewMixin


class HomeView(LoginRequiredMixin, HtmxViewMixin, TemplateView):
    template_name = "gratify/home.html"


class PreviewView(LoginRequiredMixin, TemplateView):
    template_name = "gratify/preview.html"


class SubscriptionsView(HtmxViewMixin, LoginRequiredMixin, TemplateView):
    template_name = "gratify/subscriptions.html"
