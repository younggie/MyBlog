from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    attach = models.ImageField(upload_to="photos", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_date",)
