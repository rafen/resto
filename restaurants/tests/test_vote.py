import factory
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurants.factories import UserFactory, RestaurantFactory, CommentFactory
from restaurants.models import Restaurant
from restaurants.tests.base import BaseAPITestCase

COMMENT_BATCH = 4


class VoteTest(BaseAPITestCase):

    def setUp(self):
        super(VoteTest, self).setUp()
        # Create a restaurants
        self.restaurant = RestaurantFactory.create()
        self.restaurant.save()
        # Get views urls
        self.vote_url = reverse('restaurant-vote', args=(self.restaurant.pk,))

    def test_vote_permissions(self):
        response = self.client.post(self.vote_url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_vote(self):
        self._login()
        # Thumbs Up a restaurant
        response = self.client.put(self.vote_url, {
            'vote': True,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.restaurant.votes.count(), 1)
        # Thumbs Down
        response = self.client.put(self.vote_url, {
            'vote': False,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.restaurant.votes.count(), 0)



