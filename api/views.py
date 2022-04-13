from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from .models import User
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# Create your views here.
auth_url = r"https://discord.com/api/oauth2/authorize?client_id=962670671572381737&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fapi%2Flogin%2Fredirect%2F&response_type=code&scope=identify%20email"

def login(request):
    return redirect(auth_url)
@api_view(["GET"])
def login_redirect(request):
    code = request.GET.get('code')
    credentials = exchange_code(code)
    user = User.objects.filter(id=credentials["id"])
    if not len(user):
        new_user = User(
            id = credentials['id'],
            discord_id = f"{credentials['username']}#{credentials['discriminator']}",
            avatar = credentials['avatar'],
            email = credentials['email'],
            name = "",
            wordle = 0,
            papertoss = 0,
            points_spent = 0
        )
        new_user.save()
        print(new_user)
        new_user_json = UserSerializer(new_user, many=False).data
        return JsonResponse(new_user_json)
    user = user.first()
    print(user)
    print(user.discord_id)
    user_json = UserSerializer(user, many=False).data
    print(user_json)
    return Response(user.discord_id)


@api_view(["POST"])
def user_details(request):
    id = request.data["discord_id"]
    user = User.objects.get(discord_id=id)
    user_data = UserSerializer(user, many=False)
    return Response(user_data.data)


def exchange_code(code):
    data = {
        "client_id": r"962670671572381737",
        "client_secret": r"OJTNkk3dyGo1ylhn_IGkKYLQVifqiFFA",
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': r'http://localhost:8000/api/login/redirect/',
        'scope': 'identity email'
    }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(r'https://discord.com/api/oauth2/token', data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/users/@me", headers= {
        'Authorization': f'Bearer {access_token}' 
    })
    return response.json()