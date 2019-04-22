from django.contrib import admin

from . import models


class AliasInline(admin.TabularInline):
    model = models.Alias
    search_fields = ['name']
    list_display = ['name', 'person']
    extra = 1


class TitleInline(admin.TabularInline):
    model = models.Title
    search_fields = ['name']
    list_display = ['name', 'person']
    extra = 1


class DeathCauseAdmin(admin.ModelAdmin):
    model = models.DeathCause
    list_display = ['id', 'description']
    search_fields = ['description']
    list_editable = ['description']
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    model = models.Person
    search_fields = [
        'first_name',
        'last_name',
    ]
    autocomplete_fields = [
        'house',
        'mother',
        'father',
        'spouse',
        'cause_of_death',
        'murdered_by',
    ]
    inlines = [
        TitleInline,
        AliasInline,
    ]
    list_display = [
        '__str__',
        'house',
        'sibling_order',
        'mother',
        'father',
        'spouse',
    ]
    list_editable = [
        'sibling_order',
        'mother',
        'father',
        'spouse',
    ]
    list_filter = [
        'house',
        'is_dead',
    ]


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.DeathCause, DeathCauseAdmin)
