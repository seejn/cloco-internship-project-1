from django.shortcuts import render
from django.http import JsonResponse
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import jwt, math, time

from users.models import CustomUser
from users.views import UserSerializer
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
                return JsonResponse({"message": "User not Authorized"}, status=401)
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

def PostSerializer(obj):
    fields = ["id", "title", "content", "post_image", "is_deleted", "like_count", "created_at"]
    values = [obj.id, obj.title, obj.content, obj.post_image, obj.is_deleted, obj.like_count, obj.created_at]

    # data = dict(zip(fields,values))
    data = {k:v for k,v in zip(fields,values)}
    return data

def get_all_posts(request):
    method = "GET"
    if not request.method == method:
        return JsonResponse({"message": "Not appropriate request method"}, status=405)

    all_posts = Post.objects.all()
    # all_posts = [PostSerializer(post) for post in all_posts]
    posts = []
    for post in all_posts:
        user = UserSerializer(post.get_user())
        post = PostSerializer(post)

        post["user"] = user
        posts.append(post)

    return JsonResponse({"message": "All posts", "data": posts})

@login_required
def get_user_post(request):
    method = "GET"
    if not request.method == method:
        return JsonResponse({"message": "Not appropriate request method"}, status=405)
    return JsonResponse({"message": "get user post request success"}, status=200)


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
