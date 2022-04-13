from distutils.command.config import config
from django.shortcuts import redirect
from .models import User
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from dotenv import dotenv_values
from django.conf import settings
# Create your views here.

env_path = str(settings.BASE_DIR) + r"/.env"
config = dotenv_values(env_path)
auth_url = config["auth_url"]

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
            wordle = 0,
            papertoss = 0,
            total_score = 0
        )
        new_user.save()
        new_user_json = UserSerializer(new_user, many=False).data
        rank = User.objects.filter(total_score__gte=new_user.total_score).count()
        return Response({"user": new_user_json, "rank": rank})
    user = user.first()
    user_json = UserSerializer(user, many=False).data
    rank = User.objects.filter(total_score__gte=user.total_score).count()
    return Response({"user": user_json, "rank": rank})


@api_view(["POST"])
def user_details(request):

    id = request.data["discord_id"]
    user = User.objects.get(discord_id=id)
    user_data = UserSerializer(user, many=False)
    return Response(user_data.data)


def exchange_code(code):
    data = {
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
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