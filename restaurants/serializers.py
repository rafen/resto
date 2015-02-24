from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from restaurants.models import Restaurant, Visit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id', 'user', 'restaurant', 'created')


class VisitRelatedSerializer(VisitSerializer):
    user = UserSerializer(many=False, read_only=True)


class RestaurantSerializer(serializers.ModelSerializer):
    visitors = VisitRelatedSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'visitors')
