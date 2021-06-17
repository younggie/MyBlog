from django.db import models
from django.urls import reverse


class Like(models.Model):

    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        "users.User", related_name="likes", on_delete=models.CASCADE
    )
    posts = models.ManyToManyField("posts.Post", related_name="likes", blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def count_posts(self):
        return self.posts.count()

    count_posts.short_description = "좋아요 갯수"    