from django.conf.urls import url

from rest_framework import routers
from . import views


# this is DRF router for REST API viewsets
router = routers.DefaultRouter()
# register REST API endpoints with DRF router
#router.register(r'place', PlaceViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    url(r'^$',views.PlaceView.as_view()),
    ]