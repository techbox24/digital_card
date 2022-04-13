from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from api.models import User
from api.serializers import ScoreSerializer


@api_view(['GET'])
def GetData(request):
    data = User.objects.all()
    serializer = ScoreSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def UpdateScore(request):
    data = request.data
    print(User.objects.get(discord_id=data['discord_id']))
    user = User.objects.get(discord_id=data['discord_id'])
    user.papertoss = int(user.papertoss) + int(data['score'])
    user.save()
    serializer = ScoreSerializer(user, many=False)
    return Response(serializer.user)
