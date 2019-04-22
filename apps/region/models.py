from django.db import models

from core.models import TimeStampedModel


# Choices
CONTINENT_CHOICES = (
    ('Westeros', 'Westeros',),
    ('Essos', 'Essos',),
    ('Unknown', 'Unknown',),
)


class Region(TimeStampedModel):
    """Region"""
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES)

    class Meta:
        ordering = ['name', 'continent']

    def __str__(self):
        return self.name
