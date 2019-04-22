from django.contrib import admin

from . import models


class RegionAdmin(admin.ModelAdmin):
    model = models.Region
    list_display = ['id', 'name', 'continent', 'description']
    search_fields = ['name']
    list_editable = [
        'name',
        'continent',
    ]
    list_filter = [
        'continent',
    ]


admin.site.register(models.Region, RegionAdmin)
