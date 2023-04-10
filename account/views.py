from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import UserSerializer

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def sign_up(req, *args, **kwargs):
    ser = UserSerializer(data=req.data)
    if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def test_access(req):
    return Response({'we': 'HERE'})