from django.db import models
from datetime import datetime
from users.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    post_image = models.CharField(max_length=250, default="image.png")
    created_at = models.DateTimeField(default=datetime.now())
    is_deleted = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="post")

    class Meta:
        db_table="posts"

    def get_user(self):
        return self.user

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now())
    is_deleted = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.content