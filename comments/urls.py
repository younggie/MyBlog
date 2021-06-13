from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("comment/create/<int:post>", views.create_comment, name="create"),
]
