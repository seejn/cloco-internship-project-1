from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import login, logout

from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from .models import CustomUser

import json, jwt, math, time


def generate_token(t_type, data, expiry_in_seconds):
    expiry = math.floor(time.time()) + expiry_in_seconds

    payload = {
        "token_type": t_type,
        "id": data.get("id"),
        "exp": expiry,
        "iat": math.floor(time.time())
    }

    token = jwt.encode(payload, 'secret', algorithm="HS256")
    return token

def decode_jwt_token(token):
    payload = jwt.decode(token, "secret", algorithms=["HS256"])
    return payload

def token_validation(request):
    token = request.COOKIES.get("access_token")

    if not token:
        return False

    return decode_jwt_token(token)

def login_handle_cookie(request):
    token = request.COOKIES.get("access_token")

    if not token:
        return False

    payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    print("paylaod", payload)
    user_id = payload.get("id")
    print("user_id", user_id)
    user = CustomUser.objects.get(pk=user_id)

    return user


def UserSerializer(obj):
    fields = ["id", "email", "username", "firstname", "lastname", "last_login", "date_joined"]
    values = [obj.id, obj.email, obj.username, obj.first_name, obj.last_name, obj.last_login, obj.date_joined]

    # data = dict(zip(fields,values))
    data = {k:v for k,v in zip(fields,values)}
    return data

# check method
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
    
    try:
        user = login_handle_cookie(request)
        if user:
            user = UserSerializer(user)

            return JsonResponse({"message": "Authentication with token", "data": user}, status=200)
    except ExpiredSignatureError:
        response = JsonResponse({"message": "Token Expired"}, status=400)
        response.delete_cookie("access_token")
        return response
    except InvalidTokenError:
        response = JsonResponse({"message": "Invalid token"}, status=400)
        response.delete_cookie("access_token")
        return response

    if not bool(request.body):
        return JsonResponse({"message": "Required fields not Found"}, status=400)

    data = json.loads(request.body)

    email = data.get("email")
    password = data.get("password")

    user = authenticate(email, password)
    if not user:
        return JsonResponse({"message": "email or password is incorrect"}, status=401)

    payload = {
        "id": user.id
    }
    user = UserSerializer(user)
    token = generate_token("access", payload, 3600)

    response = JsonResponse({"message": "login success", "data": user}, status=200)
    response.set_cookie("access_token", token)
    return response


@login_required
def sign_out(request):
    print("signout request hit")
    response = JsonResponse({"message": "You're signed out"}, status=200)
    response.delete_cookie("access_token")
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
    
    token = request.COOKIES.get("token")
    payload = decode_jwt_token(token)
    user_id = payload.get("id")


    return JsonResponse({"message": "delete user request success"}, status=200)

@csrf_exempt
@login_required
def update_user(request):
    method = "PATCH"
    if not request.method == method:
        return JsonResponse({"message": "not appropriate request"}, status=405)
    
    token = request.COOKIES.get("token")
    payload = decode_jwt_token(token)
    user_id = payload.get("id")

    return JsonResponse({"message": "update user request success"}, status=200)