from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=20, blank=True, verbose_name="이름")

    def __str__(self):
        return self.email
