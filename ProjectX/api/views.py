from rest_framework_mongoengine import viewsets

from serializers import PlaceSerializer
from models import Place

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.all()


class PlaceView(APIView):

    def get(self, request):
        """
        API endpoint that allows user to get places.
        """
        serializer = PlaceSerializer(Place.objects.all(), many=True)
        print Place.objects.all()
        response = {"places": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        print data
        serializer = PlaceSerializer(data=data)
        print serializer.is_valid()
        if serializer.is_valid():
            poll = Place(**data)
            poll.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)