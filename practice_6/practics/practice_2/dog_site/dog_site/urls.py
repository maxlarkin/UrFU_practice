"""
URL configuration for dog_site project.
"""
from django.contrib import admin
from django.urls import path
from dog_info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dog_list, name='dog_list'),
]
