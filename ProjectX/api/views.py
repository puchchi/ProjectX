from rest_framework_mongoengine import viewsets

from serializers import PlaceSerializer
from models import Place2 as db
from dataAdmin import views as dataAdminViews

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.request import QueryDict

import json

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return db.objects.all()


class PlaceView(APIView):

    def get(self, request):
        """
        API endpoint that allows user to get places.
        """
        rawData = request.GET
        if (type(rawData)==QueryDict):
            data = rawData.dict()
            query = data['search_query']
            serializer = PlaceSerializer(db.objects.search_text(query), many=True)
            response = {"places": serializer.data}
            print serializer.data
            return Response(response, status=status.HTTP_200_OK)

        serializer = PlaceSerializer(db.objects.all(), many=True)
        response = {"places": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        rawData = request.data
        data = {}
        if (type(rawData)==QueryDict):
            rawDataDict = rawData.dict()
            data["name"] = rawDataDict["place_name"].encode()
            data["state"] = rawDataDict["state"].encode()
            data["country"] = rawDataDict["country"].encode()
            data["address"] = rawDataDict["address"].encode()
            data["latitude"] = float(rawDataDict["latitude"].encode())
            data["longitude"] = float(rawDataDict["longitude"].encode())
            data["place_id"] = rawDataDict["place_id"].encode()
            data["map_url"] = rawDataDict["map_url"].encode()
            data["description"] = rawDataDict["description"].encode()
            if (data["description"]==''):
                data["description"] = data["name"] 
            photo_urls = []
            for key in rawDataDict.keys():
                if (key.find("place_photo_url")!=-1):
                    url = {}
                    url["url"] = rawDataDict[key].encode()
                    photo_urls.append(url)
            data["photo_urls"] = photo_urls
        else:
            data = rawData
        #print data
        serializer = PlaceSerializer(data=data)
        print serializer.is_valid()
        if serializer.is_valid():
            place = db(**data)
            place.save()
            if (type(rawData)==QueryDict):
                msg = data["name"] + " added successfully."
                return dataAdminViews.addPlace(request, msg, True)
            else:
                response = serializer.data
                return Response(response, status=status.HTTP_200_OK)
        else:
            if (type(rawData)==QueryDict):
                msg = "Couldn't add " + data["name"] + ". Errors: " + str(serializer.errors)
                return dataAdminViews.addPlace(request, msg, False)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)