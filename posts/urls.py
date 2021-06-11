from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index),
    path("write", views.write),
    path("<int:id>", views.read, name="read"),
]
