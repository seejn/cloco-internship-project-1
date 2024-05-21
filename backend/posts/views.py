from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

import json, jwt, math, time

from users.models import CustomUser
from posts.serializer import PostSerializer
from users.serializer import UserSerializer
from .models import Post, Comment

from tokens.models import Token
from tokens.views import check_auth_token


# check method
def login_required(func):
    def wrapper(request, *args, **kwargs):
        
        if check_auth_token(request):
            return func(request, *args, **kwargs)

        return JsonResponse({"message": "Authorization Failed"}, status=401)

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
        user = check_auth_token(request)

        new_post = user.create_post(title=title, content=content)

        new_post = PostSerializer(new_post)
    except:
        return JsonResponse({"message": "Something went wrong"}, status=500)
        

    return JsonResponse({"message": "Post published", "data": new_post}, status=200)

@csrf_exempt
@login_required
def delete_post(request, post_id):
    method = "DELETE" 
    if not request.method == method:
        return JsonResponse({"message": "Not appropriate request method"}, status=405)
    
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
        posts = Post.objects.all()
        posts = [PostSerializer(post) for post in posts]
    except:
        return JsonResponse({"message": "Something went wrong"}, status=500)

    return JsonResponse({"message": "Delete Post success", "data": posts}, status=200)
