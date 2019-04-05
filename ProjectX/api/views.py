from serializers import PlaceSerializer
from models import Place2 as db
from dataAdmin import views as dataAdminViews

from rest_framework_mongoengine import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.request import QueryDict
from django.shortcuts import get_object_or_404
import json, urllib2

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
            len = serializer.instance.__len__()
            message = str(len) + " place found"
            if rawData.has_key("_method"):
                if rawData["_method"] == 'update':
                    return dataAdminViews.updatePlace(request, serializer.data[:], message)
                if rawData["_method"] == 'delete':
                    return dataAdminViews.deletePlace(request, serializer.data[:], message)
        
        # else (calls coming from django_rest_framework)
        serializer = PlaceSerializer(db.objects.all(), many=True)
        response = {"places": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        rawData = request.data
        data = {}
        if (type(rawData)==QueryDict):
            rawDataDict = rawData.dict()
            
            if (rawDataDict.has_key("_method")):
                if (rawDataDict["_method"] == "update"):
                    return self.update(request, rawDataDict)
                elif (rawDataDict["_method"] == "delete"):
                    return self.delete(request, rawDataDict)
            else:   
                return self.create(request, rawData)

        else:
            #data = rawData
            return self.create(rawData)

    def update(self, request, dataDict):
        dbID = dataDict["db_id"]
        placeInstance = get_object_or_404(db.objects.all(), pk=dbID)
        serializer = PlaceSerializer()
        placeInstance = serializer.update(placeInstance, dataDict)
        message = "Success: '{}' updated successfully".format(placeInstance.name)
        return dataAdminViews.updatePlace(request, [], message)

    def delete(self, request, dataDict):
        dbID = dataDict["db_id"]
        placeInstance = get_object_or_404(db.objects.all(), pk=dbID)
        placeInstance.delete()
        message = "Success: '{}' deleted successfully".format(placeInstance.name)
        return dataAdminViews.deletePlace(request, [], message)

    def create(self, request, rawData):
        data = {}
        if (type(rawData)==QueryDict):
            rawDataDict = rawData.dict()

            data["name"] = rawDataDict["place_name"]
            data["state"] = rawDataDict["state"]
            data["country"] = rawDataDict["country"]
            data["address"] = rawDataDict["address"]
            data["latitude"] = float(rawDataDict["latitude"])
            data["longitude"] = float(rawDataDict["longitude"])
            data["place_id"] = rawDataDict["place_id"]
            data["map_url"] = rawDataDict["map_url"]
            data["description"] = rawDataDict["description"]
            if (data["description"]==''):
                data["description"] = data["name"] 
            photo_urls = []
            for key in rawDataDict.keys():
                if (key.find("place_photo_url")!=-1):
                    urlDict = {}
                    urlDict["url"] = getOriginalURL(rawDataDict[key])
                    photo_urls.append(urlDict)
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

def getOriginalURL(url):
    # here we will open photo url, then google will redirect us to original google content
    # url for that photos. This will help us in saving multiple call to get same photo in 
    # future using API_KEY
    response = urllib2.urlopen(url)
    return response.geturl()