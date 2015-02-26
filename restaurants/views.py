from django.views.generic import ListView
from django.http import Http404
from rest_framework import routers, serializers, viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from restaurants.models import Restaurant, Visit, Comment
from restaurants.serializers import (
    RestaurantSerializer, VisitSerializer, CommentSerializer, RestaurantVoteSerializer
)

# HTML Views

class RestaurantListView(ListView):
    """
    Default landing page served by Django.
    It will render a basic html page as a landing page.
    """
    context_object_name = 'restaurant_list'
    queryset = Restaurant.objects.filter(active=True)[:50]
    template_name = "index.html"

# API Views

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API view that display/manage the list of Restaurants
    """
    queryset = Restaurant.objects.filter(active=True)
    serializer_class = RestaurantSerializer


class VisitViewSet(viewsets.ModelViewSet):
    """
    API view that display/manage the list of Visits of Restaurants
    """
    queryset = Visit.objects.filter(restaurant__active=True)
    serializer_class = VisitSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API view that display/manage the list of Comments for Restaurants
    """
    queryset = Comment.objects.filter(restaurant__active=True)
    serializer_class = CommentSerializer


class RestaurantVoteView(APIView):
    """
    Vote or get the vote count.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        return Response({'votes': restaurant.votes.count()})

    def put(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantVoteSerializer(data=request.data)
        if serializer.is_valid():
            # if vote is True is Thumbs up, else Thumbs Down
            if serializer.data['vote']:
                restaurant.votes.up(request.user)
            else:
                restaurant.votes.down(request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
