from django.db import models

from core.models import TimeStampedModel
from apps.region.models import Region


class House(TimeStampedModel):
    """House

    Region <1:1> House
    """
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    sigil_description = models.TextField(null=True, blank=True)
    sigil_image_url = models.URLField(null=True, blank=True)
    motto = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['name', 'region']

    def __str__(self):
        return f'House {self.name.title()}'
