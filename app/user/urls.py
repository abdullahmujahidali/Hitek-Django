from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, AccountCreate

from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', AccountCreate.as_view()),
    router.urls,
]
