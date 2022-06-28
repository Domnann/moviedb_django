from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='moviesite'),
    path('result/', views.result, name='moviesite-result'),
]