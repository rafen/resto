from django.test import TestCase
from rest_framework.test import APIClient
from restaurants.factories import UserFactory


class BaseAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Create a super user
        self.user = UserFactory.create()
        self.user.is_superuser = True
        self.user.save()

    def _login(self):
        self.client.login(username=self.user.username, password='password')
