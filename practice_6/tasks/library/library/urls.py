"""URL configuration for library project."""
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_detail, name='book_detail')
]
