from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles_view, name='articles'),
]
