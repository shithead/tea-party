from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.bot_create, name="bot_create"),
]

