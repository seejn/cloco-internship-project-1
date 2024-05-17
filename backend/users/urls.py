from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.user_login, name=""),
    path("register/", views.register, name=""),
    path("delete/", views.delete_user, name=""),
    path("update/", views.update_user, name=""),
    
    path("signout/", views.sign_out, name=""),
]