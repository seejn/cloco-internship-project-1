from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import F

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The Email must be set")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    contact = models.CharField(max_length=50, unique=True, null=True)
    address = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "users"


    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def create_post(self, title, content):
        print(f"from create_post users models: {title} {content}")
        new_post = self.post.create(title=title, content=content)
        new_post.save()
        return new_post

    def get_posts(self):
        return self.post.all().order_by(F("created_at").desc())

    def __str__(self):
        return self.email