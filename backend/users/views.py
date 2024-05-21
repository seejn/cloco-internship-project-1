from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import login, logout

from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password


from .models import CustomUser
from tokens.models import Token
from tokens.views import check_auth_token

from posts.serializer import PostSerializer
from users.serializer import UserSerializer

import json, secrets


# check method
def login_required(func):
    def wrapper(request, *args, **kwargs):
        
        if check_auth_token(request):
            return func(request, *args, **kwargs)

        return JsonResponse({"message": "Authorization Failed"}, status=401)

    return wrapper


def authenticate(email, password):
    try:
        user = CustomUser.objects.get(email=email)
    except:
        return False

    hashed_password = user.password

    if not check_password(password, hashed_password): 
        return False

    return user

@csrf_exempt
def user_login(request):
    method = "POST"
    if not request.method == method:
        return JsonResponse({"message": "Not appropriate request method"}, status=405)
    
   
    # CHECK FOR BEARER AUTH TOKEN
    user = check_auth_token(request)
    print("check auth token", user)
    if user:
        user = UserSerializer(user) 
        return JsonResponse({"message": "Authentication with token", "data": user}, status=200)

    if not bool(request.body):
        return JsonResponse({"message": "Required fields not Found"}, status=400)

    data = json.loads(request.body)

    email = data.get("email")
    password = data.get("password")

    user = authenticate(email, password)

    if not user:
        return JsonResponse({"message": "email or password is incorrect"}, status=401)

    try:
        token = user.create_token(t_type="auth")
    except IntegrityError: 
        return JsonResponse({"message": "Token already exists"}, status=400)

    user = UserSerializer(user)

    response = JsonResponse({"message": "login success", "token": token, "data": user}, status=200)
    return response


@login_required
def sign_out(request):
    print("signout request hit")
    user = check_auth_token(request)
    user.delete_token("auth")
    user.save()

    response = JsonResponse({"message": "You're signed out"}, status=200)
    return response


@csrf_exempt
def register(request):
    method = "POST"
    if not request.method == method:
        return JsonResponse({"message": "Not appropriate request method"}, status=405)
    
    if not bool(request.body):
        return JsonResponse({"message": "Required fields not Found"}, status=400)
    
    
    data = json.loads(request.body)
    keys = [key for key in data.keys()]
    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in keys:
            return JsonResponse({"message": "Required fields not Found"}, status=400)
            
    email = data.get("email")
    password = data.get("password")

    try:
        user = CustomUser.objects.create_user(email=email, password=password)
        user = UserSerializer(user)
    except IntegrityError:
        return JsonResponse({"message": "User Already Exists"}, status=403)

    return JsonResponse({"message": "New user created", "data": user}, status=201)

@csrf_exempt
@login_required
def delete_user(request):
    method = "DELETE"
    if not request.method == method:
        return JsonResponse({"message": "not appropriate request"}, status=405)
    
    user = check_auth_token(request)
    user.delete()
    user = UserSerializer(user)

    return JsonResponse({"message": "delete user request success"}, status=200)

@csrf_exempt
@login_required
def update_user(request):
    method = "PATCH"
    if not request.method == method:
        return JsonResponse({"message": "not appropriate request"}, status=405)

    data = json.loads(request.body)
    
    user = check_auth_token(request)

    user.__dict__.update(data)
    print(user)
    print(data)

    user.save()
    print(user)

    user = UserSerializer(user)

    return JsonResponse({"message": "User Updated", "data": user}, status=200)


def get_posts(request, user_id):
    method = "GET"
    if not request.method == method:
        return JsonResponse({"message": "not appropriate request"}, status=405)

    try:
        user = CustomUser.objects.get(pk=user_id)
        posts = user.get_posts()
    except:
        return JsonResponse({"message": "User not Available"}, status=404)
    
    user = UserSerializer(user)
    
    user_posts = []
    for post in posts:
        post = PostSerializer(post)
        post["user"] = user
        user_posts.append(post)

    return JsonResponse({"message": "User Post", "data": user_posts}, status=200)
