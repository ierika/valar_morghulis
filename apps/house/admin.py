from django.contrib import admin

from apps.person.models import Person
from . import models


class PersonInline(admin.TabularInline):
    model = Person
    fields = [
        'first_name',
        'last_name',
        'gender',
        'sibling_order',
        'is_dead',
        'cause_of_death',
        'nature_of_death',
    ]
    autocomplete_fields = ['cause_of_death']
    extra = 0


class HouseAdmin(admin.ModelAdmin):
    model = models.House
    list_display = [
        '__str__',
        'region',
        'description',
    ]
    inlines = [PersonInline]
    search_fields = ['name']
    autocomplete_fields = ['region']
    list_filter = [
        'region',
    ]


admin.site.register(models.House, HouseAdmin)
