from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movie-index'),
    path("search/", views.search, name="search"),
]