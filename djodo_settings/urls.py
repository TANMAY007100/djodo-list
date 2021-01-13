"""djodo_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings



urlpatterns = [
    path('', include('djodo_main.urls')),
    path(f'{settings.ADMIN_URL}/', admin.site.urls),
]
