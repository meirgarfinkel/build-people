from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path("health/", lambda request: HttpResponse("OK")),
    path("admin/", admin.site.urls),
    path("gratify/", include("gratify.urls")),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
