# Generated by Django 5.0.6 on 2024-05-17 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_comment_created_at_alter_post_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 17, 14, 26, 50, 693513)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 17, 14, 26, 50, 692595)
            ),
        ),
    ]