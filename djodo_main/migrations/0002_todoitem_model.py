# Generated by Django 3.1.5 on 2021-02-13 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('djodo_main', '0001_initial_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_uuid', models.UUIDField(default=uuid.uuid4)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'todo item',
                'verbose_name_plural': 'todo items',
                'db_table': 'todo_item',
            },
        ),
    ]
