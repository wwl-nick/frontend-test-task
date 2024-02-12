from django.contrib import admin

from apps.models import Platform, App


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    ...


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    ...
