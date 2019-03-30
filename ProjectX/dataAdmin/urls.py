from django.conf.urls import url

from . import views


# register REST API endpoints with DRF router
#router.register(r'place', PlaceViewSet)

urlpatterns = [
    #path('', include(router.urls)),
        url(r'^$',views.index, name='dataAdminIndex'),
        url(r'^index/$',views.index, name='dataAdminIndex'),
        url(r'^addplace/$',views.addPlace, name='dataAdminAddPlace'),
    ]
