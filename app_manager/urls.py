from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app_manager.yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('api/', include('apps.urls')),
    path('api/doc/', include(yasg_urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
