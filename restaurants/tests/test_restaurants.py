import factory
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurants.factories import UserFactory, RestaurantFactory, VisitFactory

RESTAURANT_BATCH = 4



class RestaurantsTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Create a super user
        self.user = UserFactory.create()
        self.user.is_superuser = True
        self.user.save()
        # Create a batch of restaurants
        self.restaurants = RestaurantFactory.create_batch(RESTAURANT_BATCH)
        [r.save() for r in self.restaurants]
        # Get views urls
        self.restaurant_url = reverse('restaurant-list')

    def _login(self):
        self.client.login(username=self.user.username, password='password')

    def test_restaurant_list_filter_by_active(self):
        # Make one restaurant inactive
        restaurant = self.restaurants[0]
        restaurant.active = False
        restaurant.save()
        # Send request to server
        response = self.client.get(self.restaurant_url)
        # Check that the restaurant is not returned in the list
        self.assertEquals(response.data['count'], RESTAURANT_BATCH-1)

    def test_restaurant_creation_permissions(self):
        response = self.client.post(self.restaurant_url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_restaurant_creation_permissions_ok(self):
        self._login()
        response = self.client.post(self.restaurant_url, {
            'name': 'Pizza resto',
            'description': 'Good Pizza!'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_restaurant_visitors(self):
        # Create a visit to a restaurant
        restaurant = self.restaurants[0]
        visit = VisitFactory.create(restaurant=restaurant)
        visit.save()
        # Ask for the restaurant details
        response = self.client.get(reverse('restaurant-detail', args=(visit.restaurant.id,)))
        # Check the if the visit is displayed
        self.assertTrue(response.data['visitors'])


