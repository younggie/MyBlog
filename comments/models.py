from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        "users.User", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        "posts.Post", related_name="comments", on_delete=models.CASCADE
    )
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
