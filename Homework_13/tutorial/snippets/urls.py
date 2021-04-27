from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from . import views
from .views import SnippetViewSet

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]