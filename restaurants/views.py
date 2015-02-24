from django.views.generic import ListView
from rest_framework import routers, serializers, viewsets
from restaurants.models import Restaurant, Visit
from restaurants.serializers import RestaurantSerializer, VisitSerializer


class RestaurantListView(ListView):
    """
    Default landing page served by Django.
    It will render a basic html page as a landing page.
    """
    context_object_name = 'restaurant_list'
    queryset = Restaurant.objects.filter(active=True)
    template_name = "index.html"


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API view that display/manage the list of Restaurants
    """
    queryset = Restaurant.objects.filter(active=True)
    serializer_class = RestaurantSerializer


class VisitViewSet(viewsets.ModelViewSet):
    """
    API view that display/manage the list of Visits
    """
    queryset = Visit.objects.filter(restaurant__active=True)
    serializer_class = VisitSerializer

