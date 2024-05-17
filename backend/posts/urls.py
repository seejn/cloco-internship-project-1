from django.urls import path
from . import views

urlpatterns = [
    path("get_all_posts/", views.get_all_posts, name="")
]