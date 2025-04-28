from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from hx_requests.views import HtmxViewMixin
from django.db.models import OuterRef, Exists
from urllib.parse import unquote

from build_people.models import Recognition


class HomeView(LoginRequiredMixin, HtmxViewMixin, ListView):
    template_name = "build_people/home.html"
    model = Recognition
    context_object_name = "recognitions"

    def get_queryset(self):
        user = self.request.user
        hearts_qs = Recognition.objects.filter(id=OuterRef("pk"), hearts=user)

        return (
            Recognition.objects.filter(created_by__company=user.company)
            .select_related("created_by")
            .annotate(hearted_by_user=Exists(hearts_qs))
            .prefetch_related("hearts", "comments")
            .order_by("-created_at")
        )


class PreviewView(LoginRequiredMixin, TemplateView):
    template_name = "build_people/preview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = self.request.GET.get("url", "http://localhost:8000/")
        
        # Add the URL to the context
        context["url"] = unquote(url)
        return context


class SubscriptionsView(HtmxViewMixin, LoginRequiredMixin, TemplateView):
    template_name = "build_people/subscriptions.html"


class CoreValuesView(HtmxViewMixin, LoginRequiredMixin, TemplateView):
    template_name = "build_people/core_values_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["core_values"] = self.request.user.company.core_values.all()
        return context


class ProfileView(HtmxViewMixin, LoginRequiredMixin, TemplateView):
    template_name = "build_people/profile.html"
