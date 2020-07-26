from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.FileField(upload_to='avatar/', blank=True, null=True)

    def __str__(self):
        return self.email
