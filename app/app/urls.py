"""app URL Configuration."""

# Django
from django.contrib import admin
from django.urls import path, include
from django.http.response import HttpResponse
from django.core.management import call_command

from user.views import AccountCreate

from user.urls import router

# 3rd Party Libraries
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def refresh_db(request):
    """Clears Database, runs migrations and then generates fake data."""
    call_command("drop_all_tables")
    call_command("automate")
    call_command("generate_fake_data")
    return HttpResponse(status=200)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/user/', include(router.urls)),
    path('api/v1/user/newuser/', AccountCreate.as_view(), name="admin-user"),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
