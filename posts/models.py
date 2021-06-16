from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, null=False)
    
    attach = models.ImageField(upload_to="photos", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True,null=True)
    

    class Meta:
        ordering = ("-created_date",)

    def get_absolute_url(self):
        return reverse("posts:read", kwargs={"pk": self.pk})
