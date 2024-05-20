from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from django.db.models import F

import json, jwt, math, time

from users.models import CustomUser
from posts.serializer import PostSerializer
from users.serializer import UserSerializer
from .models import Post, Comment


def decode_jwt_token(token):
    payload = jwt.decode(token, "secret", algorithms=["HS256"])
    return payload

def token_validation(request):
    token = request.COOKIES.get("access_token")

    if not token:
        return False

    return decode_jwt_token(token)

def login_required(func):
    def wrapper(request, *args, **kwargs):
        try:
            payload = token_validation(request)
            if not payload:
                return JsonResponse({"message": "Login again"}, status=401)
        except ExpiredSignatureError:
            response = JsonResponse({"message": "Token Expired"}, status=400)
            response.delete_cookie("access_token")
            return response
        except InvalidTokenError:
            response = JsonResponse({"message": "Invalid token"}, status=400)
            response.delete_cookie("access_token")
            return response
            
        return func(request, *args, **kwargs)

    return wrapper


def get_all_posts(request):
    method = "GET"
    if not request.method == method:
        return JsonResponse({"message": "Not appropriate request method"}, status=405)

    all_posts = Post.objects.all().order_by(F("created_at").desc())
    # all_posts = [PostSerializer(post) for post in all_posts]
    posts = []
    for post in all_posts:
        user = UserSerializer(post.get_user())
        post = PostSerializer(post)

        post["user"] = user
        posts.append(post)

    return JsonResponse({"message": "All posts", "data": posts})

def get_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        posted_by = post.user
    except:
        return JsonResponse({"message": "post not found"}, status=404)

    post = PostSerializer(post)
    posted_by = UserSerializer(posted_by)
    post["posted_by"] = posted_by
    return JsonResponse({"message": "Post", "data": post}, status=200)



@csrf_exempt
@login_required
def create_post(request):
    method = "POST" 
    if not request.method == method:
        return JsonResponse({"message": "Not appropriate request method"}, status=405)

    data = json.loads(request.body)

    print(request.body)

    title = data.get("title")
    content = data.get("content")
    print(f"From post create_post: {title}, {content}")
    try:
        token = request.COOKIES.get("access_token")
        payload = decode_jwt_token(token)
        user_id = payload.get("id")

        user = CustomUser.objects.get(pk=user_id)

        new_post = user.create_post(title=title, content=content)

        new_post = PostSerializer(new_post)
    except:
        return JsonResponse({"message": "Something went wrong"}, status=500)
        

    return JsonResponse({"message": "Post published", "data": new_post}, status=200)