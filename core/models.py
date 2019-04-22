from django.db import models


class TimeStampedModel(models.Model):
    """Core timestamped model"""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
