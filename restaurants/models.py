from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    picture = models.ImageField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return u'%s (%s)' % (slugify(self.name), self.id)

    # def get_absolute_url(self):
    #     return reverse('detail_image_study', args=[str(self.id)])


class Visit(models.Model):
    """
    Store visits of users to Restaurant.
    For simplicity the user doesn't need to enter the date of the visit
    the system only store the creation date of the visit.
    """
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant, related_name='visitors')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s (%s)' % (self.user, self.created)


class Comment(models.Model):
    """
    Custom comment model specific for Restaurant.
    Let's keep it simple and stupid.
    """
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant, related_name='comments')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s - %s' % (self.user, self.restaurant)

