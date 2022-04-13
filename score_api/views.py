import os

from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User
from api.serializers import ScoreSerializer

load_dotenv("E:\PROJECTS\digital_card_main\.env")


@api_view(['GET'])
def GetData(request):
    data = User.objects.all()
    serializer = ScoreSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def UpdateScore(request):
    data = request.data
    if os.getenv('token') == data['token']:
        user = User.objects.get(discord_id=data['discord_id'])
        user.papertoss = int(user.papertoss) + int(data['score'])
        user.save()
        serializer = ScoreSerializer(user, many=False)
        return Response(serializer.data)
    return Response({"Response": "Token id is Wrong"})
