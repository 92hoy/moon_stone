from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    # path('', include('backend.urls')),
    path('', include('main.urls')),
]