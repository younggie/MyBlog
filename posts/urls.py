from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index),
    path("write", views.PostWriteView.as_view(), name="write"),
    path("<int:pk>/edit/", views.PostEditView.as_view(), name="edit"),
    path("<int:pk>", views.PostReadView.as_view(), name="read"),
]
