import factory
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurants.factories import UserFactory, RestaurantFactory, CommentFactory
from restaurants.models import Restaurant
from restaurants.tests.base import BaseAPITestCase


class UserTest(BaseAPITestCase):

    def test_current_user_logout(self):
        url = reverse('current-user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_current_user_login(self):
        url = reverse('current-user')
        self._login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_user_creation_permissions(self):
        url = reverse('user-list')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

