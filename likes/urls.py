from django.urls import path
from . import views

app_name = "likes"

urlpatterns = [
    path("toggle/<int:post_pk>", views.toggle_like, name="toggle-like"),
   
]
