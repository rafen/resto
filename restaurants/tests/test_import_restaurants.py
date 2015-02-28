from django.core.management import call_command
from django.test import TestCase
import json
import mock
from restaurants.models import Restaurant


class FakeFactual(object):

    def __init__(self, *args, **kwargs):
        # Load factual example restaurants from file
        f = open('restaurants/tests/restos.json', 'r')
        self.restoData = json.loads(f.read())

    def table(self, *args, **kwargs):
        return self

    def filters(self, *args, **kwargs):
        return self

    def include_count(self, *args, **kwargs):
        return self

    def limit(self, *args, **kwargs):
        return self

    def offset(self, *args, **kwargs):
        return self

    def total_row_count(self):
        return 2

    def data(self):
        return self.restoData


class CommandsTestCase(TestCase):

    @mock.patch('factual.Factual', FakeFactual)
    def test_restaurant_import(self):
        call_command('import_restaurants')

        factual = FakeFactual()
        self.assertEqual(Restaurant.objects.count(), len(factual.restoData))
        # test restaurant content generated correctly
        for resto in factual.restoData:
            resto_obj = Restaurant.objects.get(identifier=resto['factual_id'])
            self.assertEqual(resto_obj.name, resto['name'])
            self.assertEqual(resto_obj.rating, resto['rating'])

    @mock.patch('factual.Factual', FakeFactual)
    def test_restaurant_import_twice(self):
        call_command('import_restaurants')
        call_command('import_restaurants')

        factual = FakeFactual()
        self.assertEqual(Restaurant.objects.count(), len(factual.restoData))
