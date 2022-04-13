# Create your views here.
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User
from api.serializers import ScoreSerializer


def creating_obj(game):
    a = User.objects.order_by(f'-{game}')
    serializer = ScoreSerializer(a, many=True)
    return serializer.data


@api_view(['POST'])
def GetData(request):
    data = request.data
    if data['game'] == 'papertoss':
        board = creating_obj('papertoss')
        return Response(board)
    elif data['game'] == 'total':
        board = creating_obj('total_score')
        return Response(board)
    return Response({"Response" : "Wrong game name!!!!!"})
