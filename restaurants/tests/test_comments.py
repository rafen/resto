import factory
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurants.factories import UserFactory, RestaurantFactory, CommentFactory
from restaurants.models import Restaurant
from restaurants.tests.base import BaseAPITestCase

COMMENT_BATCH = 4


class VisitsTest(BaseAPITestCase):

    def setUp(self):
        super(VisitsTest, self).setUp()
        # Create a restaurants
        self.restaurant = RestaurantFactory.create()
        self.restaurant.save()
        # Create a batch of visits
        self.comments = CommentFactory.create_batch(COMMENT_BATCH, restaurant=self.restaurant)
        [c.save() for c in self.comments]
        # Get views urls
        self.comment_url = reverse('comment-list')

    def test_comment_creation_permissions(self):
        response = self.client.post(self.comment_url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_comment_creation_permissions_ok(self):
        self._login()
        response = self.client.post(self.comment_url, {
            'user': self.user.id,
            'restaurant': self.restaurant.id,
            'comment': 'good restaurant!'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        comments = Restaurant.objects.get(id=self.restaurant.id).comments.all()
        self.assertEqual(comments[0].user, self.user)


