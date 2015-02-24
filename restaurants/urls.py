from django.conf.urls import patterns, include, url
from rest_framework import routers
from restaurants.views import RestaurantViewSet, VisitViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'visits', VisitViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)