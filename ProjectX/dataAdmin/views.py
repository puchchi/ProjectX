from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from datetime import datetime
from ProjectX.projectxdefs import *


# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'data_admin/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

def addPlace(request, msg="", isSuccessful=False):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    if not isValidDataAdmin(request.user.username):
        return render( request,
        'data_admin/message.html',
        {
            'message':'Unauthorised user.'
        }
    )
    
    return render(
        request,
        'data_admin/add_place.html',
        {
            'title':'Add Place',
            'year':datetime.now().year,
            'key':GOOGLE_API_KEY,
            'placeAPI':'http://localhost:8000/api/',
            'previousPostStatus': isSuccessful,
            'previousMessage':msg
        }
    )

def updatePlace(request, serializer=[], msg=""):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    if not isValidDataAdmin(request.user.username):
        return render( request,
        'data_admin/message.html',
        {
            'message':'Unauthorised user.'
        }
    )
    # serializer if ordered dict, we need to convert it to dict
    place_list=[]
    for place in serializer:
        placeDict = dict(place)
        photo_urls = []
        for photo_url in placeDict['photo_urls']:
            photo_urls.append(dict(photo_url))
        placeDict['photo_urls'] = photo_urls
        place_list.append(placeDict)

    return render(
        request,
        'data_admin/update_place.html',
        {
            'title':'Update Place',
            'place_list':place_list,
            'method':'update',
            'previousMessage':msg
        }
    )

def deletePlace(request, serializer=[], msg=""):
    return updatePlace(request, serializer, msg)

def isValidDataAdmin(userName):
    for name in VALID_DATA_ADMIN_LIST:
        if name == userName:
            return True

    return False