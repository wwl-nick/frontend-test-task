from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps import views

app_name = 'apps'

router = DefaultRouter()
router.register('apps', views.AppViewSet, basename='apps')
router.register('platforms', views.PlatformViewSet, basename='platforms')

urlpatterns = [
    path('', include(router.urls)),
]
