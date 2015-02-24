import factory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from restaurants.models import Restaurant, Visit, Comment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_%d" % n)
    email = factory.LazyAttribute(lambda obj: '%s@mailinator.com' % obj.username)
    password = make_password('password')


class RestaurantFactory(factory.Factory):
    name = factory.Sequence(lambda n: 'Restaurant%d' % n)
    description = factory.Sequence(lambda n: 'Restaurant description %d' % n)
    active = True

    class Meta:
        model = Restaurant


class VisitFactory(factory.Factory):
    user = factory.SubFactory(UserFactory)
    restaurant = factory.SubFactory(RestaurantFactory)

    class Meta:
        model = Visit


class CommentFactory(factory.Factory):
    user = factory.SubFactory(UserFactory)
    restaurant = factory.SubFactory(RestaurantFactory)
    comment = factory.Sequence(lambda n: 'Comment %d' % n)

    class Meta:
        model = Comment
