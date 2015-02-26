from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from restaurants.models import Restaurant, Visit, Comment


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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'restaurant', 'comment', 'created')


class CommentRelatedSerializer(CommentSerializer):
    user = UserSerializer(many=False, read_only=True)


class RestaurantSerializer(serializers.ModelSerializer):
    visitors = VisitRelatedSerializer(many=True, read_only=True)
    comments = CommentRelatedSerializer(many=True, read_only=True)
    votes = serializers.IntegerField(source='votes.count', read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'telephone', 'website',
            'description', 'visitors', 'comments', 'votes', 'rating')


class RestaurantVoteSerializer(serializers.Serializer):
    # True for Up, False for Down
    vote = serializers.BooleanField()
