import factory
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurants.factories import UserFactory, RestaurantFactory, VisitFactory
from restaurants.models import Restaurant
from restaurants.tests.base import BaseAPITestCase

VISIT_BATCH = 4


class VisitsTest(BaseAPITestCase):

    def setUp(self):
        super(VisitsTest, self).setUp()
        # Create a restaurants
        self.restaurant = RestaurantFactory.create()
        self.restaurant.save()
        # Create a batch of visits
        self.visits = VisitFactory.create_batch(VISIT_BATCH, restaurant=self.restaurant)
        [v.save() for v in self.visits]
        # Get views urls
        self.visit_url = reverse('visit-list')

    def test_visit_creation_permissions(self):
        response = self.client.post(self.visit_url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_visit_creation_permissions_ok(self):
        self._login()
        response = self.client.post(self.visit_url, {
            'user': self.user.id,
            'restaurant': self.restaurant.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        visitors = Restaurant.objects.get(id=self.restaurant.id).visitors.all()
        self.assertEqual(visitors[0].user, self.user)


