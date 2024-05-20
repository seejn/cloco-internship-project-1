from django.urls import path
from . import views

urlpatterns = [
    path("get_all_posts/", views.get_all_posts, name=""),
    path("create_post/", views.create_post, name=""),
    path('<int:post_id>/', views.get_post, name="")
]