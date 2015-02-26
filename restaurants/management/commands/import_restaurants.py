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

    def handle(self, *args, **options):
        factual = Factual(KEY, SECRET)
        # {"$and":[{"country":{"$eq":"US"}},{"region":{"$eq":"NY"}}]}
        restaurants_table = factual.table('restaurants-us')

        query = restaurants_table.filters({'$and':[{'region':{'$eq':"NY"}}]}).include_count(True)
        total = query.total_row_count()
        self.stdout.write('Ready to import %s restaurants, in %s requests' % (total, total/BATCH + total%BATCH))

        for i in range(total/BATCH + total%BATCH):
            try:
                data = query.offset(BATCH * i).limit(BATCH).data()
            except APIException as e:
                # If you are using a free version of factual, only 500 restaurant are imported
                # you need to premium account to access the complete data
                self.stdout.write('API Error: %s' % e)
                break

            for restaurant in data:
                # Get or created restaruant using factual id
                resto, created = Restaurant.objects.get_or_create(identifier=restaurant.get('factual_id'))
                # Update restaurant with new values
                resto.name = restaurant.get('name')
                resto.address = restaurant.get('address')
                resto.telephone = restaurant.get('tel')
                resto.website = restaurant.get('website')
                resto.description = ', '.join(restaurant.get('cuisine') or [])
                resto.rating = restaurant.get('rating')
                resto.save()
            self.stdout.write('Successfully imported %s restaurants' % (BATCH*i))
