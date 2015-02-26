from django.contrib import admin
from .models import Restaurant, Visit


class VisitInline(admin.StackedInline):
    model = Visit
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'telephone', 'website', 'rating', 'votes_count')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('active', 'created')
    inlines = (VisitInline,)


admin.site.register(Restaurant, RestaurantAdmin)
