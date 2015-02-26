from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurants.views import RestaurantListView


urlpatterns = patterns('',
    url(r'^$', RestaurantListView.as_view(), name='index'),
    url(r'^restaurants/', include('restaurants.urls')),

	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
