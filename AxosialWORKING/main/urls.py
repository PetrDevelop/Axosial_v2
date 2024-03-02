from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('join', views.join, name='join'),
    path('<int:pk>', views.FastDetailView.as_view(), name='FastDetail')
]
