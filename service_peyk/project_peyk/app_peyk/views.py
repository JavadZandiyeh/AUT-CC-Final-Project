from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def test(request) -> Response:

    return Response("test", status.HTTP_200_OK)
