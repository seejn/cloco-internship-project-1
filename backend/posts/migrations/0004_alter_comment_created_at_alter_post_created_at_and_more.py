# Generated by Django 5.0.6 on 2024-05-19 08:26

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_comment_created_at_alter_post_created_at"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 19, 8, 26, 43, 918924)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 19, 8, 26, 43, 917997)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
