from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index),
    path("write", views.PostWriteView.as_view(), name="write"),
    path("<int:pk>/edit/", views.PostEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_post, name="delete"),
    path("<int:pk>", views.PostReadView.as_view(), name="read"),
    path("search/", views.SearchView.as_view(), name="search"),
]
