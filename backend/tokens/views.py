from django.shortcuts import render

# Create your views here.
from .models import Token

# auth token check
def check_auth_token(request):
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        user_token = Token.objects.get(token=token)
        print("token", user_token)
        if user_token.is_token_expired():
            print("Token expired")
            return False            
    except:
        return False
    return user_token.user