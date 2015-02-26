from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from restaurants.views import (
    RestaurantViewSet, VisitViewSet, CommentViewSet, RestaurantVoteView
)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'visits', VisitViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = patterns('',
    url(r'^vote/(?P<pk>[0-9]+)/$', RestaurantVoteView.as_view(), name='restaurant-vote')
)
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^', include(router.urls)),
)
