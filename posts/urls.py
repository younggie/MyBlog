from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index),
    path("write", views.write),
    path("<int:pk>", views.PostReadView.as_view(), name="read"),
]
