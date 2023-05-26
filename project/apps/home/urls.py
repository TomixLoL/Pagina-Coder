from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path("crear-autor/", views.crear_autor, name="crear_autor"),
    path("crear-post/", views.crear_post, name="crear_post"),
]
