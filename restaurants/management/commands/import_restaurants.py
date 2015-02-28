from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from factual import Factual
from factual.api import APIException
from restaurants.models import Restaurant

KEY = getattr(settings, 'FACTUAL_KEY', 'e8fzyw7ucoc9OwszjVynRmQ5AN0ob1JOlxBfAkUo')
SECRET = getattr(settings, 'FACTUAL_SECRET', '1XeqU3YwtStf2XLLqwx9LzNcRTvYEvhlVpXMOv7v')
BATCH = 50


class Command(BaseCommand):
    help = 'This command will import all restaurants from Factual.com'

    def map_data_restaurant(self, resto, data):
        """
        Map data from factual to Restaurant model
        """
        resto.name = data.get('name')
        resto.address = data.get('address')
        resto.telephone = data.get('tel')
        resto.website = data.get('website')
        resto.description = ', '.join(data.get('cuisine') or [])
        resto.rating = data.get('rating')
        resto.save()


    def handle(self, *args, **options):
        factual = Factual(KEY, SECRET)
        restaurants_table = factual.table('restaurants-us')

        # Get all restaurants from New York
        # {"$and":[{"country":{"$eq":"US"}},{"region":{"$eq":"NY"}}]}
        query = restaurants_table.filters({'$and':[{'region':{'$eq':"NY"}}]}).include_count(True)
        total = query.total_row_count()
        cnt_requests = (total-1)/BATCH + 1
        self.stdout.write('Ready to import %s restaurants, in %s requests' % (total, cnt_requests))
        for i in range(cnt_requests):
            try:
                data = query.offset(BATCH * i).limit(BATCH).data()
            except APIException as e:
                # If you are using a free version of factual, only 500 restaurant are imported
                # you need to premium account to access the complete data
                self.stdout.write('API Error: %s' % e)
                break

            for restoData in data:
                # Get or created restaruant using factual id
                resto, created = Restaurant.objects.get_or_create(identifier=restoData.get('factual_id'))
                # Update restaurant with new values
                self.map_data_restaurant(resto, restoData)

            self.stdout.write('Successfully imported batch %s of restaurants' % i)
