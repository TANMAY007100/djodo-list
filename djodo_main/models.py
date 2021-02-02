from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    user_uuid = models.UUIDField(default=uuid4)

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
