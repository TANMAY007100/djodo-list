from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    user_uuid = models.UUIDField(default=uuid4)

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

class TodoItem(models.Model):

    item_uuid = models.UUIDField(default=uuid4)
    content = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'todo_item'
        verbose_name = 'todo item'
        verbose_name_plural = 'todo items'
