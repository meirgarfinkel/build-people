from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from hx_requests.views import HtmxViewMixin
from django.db.models import OuterRef, Exists
from urllib.parse import unquote

from gratify.models import Recognition


class HomeView(LoginRequiredMixin, HtmxViewMixin, ListView):
    template_name = "gratify/home.html"
    model = Recognition
    context_object_name = "recognitions"

    def get_queryset(self):
        user = self.request.user
        hearts_qs = Recognition.objects.filter(id=OuterRef('pk'), hearts=user)

        return (
            Recognition.objects.all()
            .annotate(hearted_by_user=Exists(hearts_qs))
            .prefetch_related("hearts")
            .prefetch_related("comments")
        )


class PreviewView(LoginRequiredMixin, TemplateView):
    template_name = "gratify/preview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = self.request.GET.get("url", "http://localhost:8000/gratify/")
        
        # Add the URL to the context
        context["url"] = unquote(url)
        return context


class SubscriptionsView(HtmxViewMixin, LoginRequiredMixin, TemplateView):
    template_name = "gratify/subscriptions.html"
