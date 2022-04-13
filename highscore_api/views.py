# Create your views here.
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User
from api.serializers import ScoreSerializer


@api_view(['GET'])
def GetData(request):
    a = User.objects.order_by('-papertoss')
    serializer = ScoreSerializer(a, many=True)
    print(serializer.data)
    return Response(serializer.data)
