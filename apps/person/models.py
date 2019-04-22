from django.db import models

from core.models import TimeStampedModel
from apps.house.models import House


# Choices
GENDER_CHOICES = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Unknown', 'Unknown'),
)
NATURE_OF_DEATH_CHOICES = (
    ('homicide', 'homicide'),
    ('suicide', 'suicide'),
    ('nature causes', 'nature causes'),
)


class DeathCause(TimeStampedModel):
    """Death cause"""
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description


class Person(TimeStampedModel):
    """Person

    House <1:M> Person
    """
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    is_dead = models.BooleanField(default=False)
    cause_of_death = models.ForeignKey(DeathCause, on_delete=models.SET_NULL,
                                       null=True, blank=True)
    nature_of_death = models.CharField(max_length=20,
                                       choices=NATURE_OF_DEATH_CHOICES,
                                       null=True,
                                       blank=True)
    murdered_by = models.ForeignKey('self', on_delete=models.SET_NULL,
                                    blank=True, null=True,
                                    related_name='self_murdered_by')
    father = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                               blank=True, related_name='self_father')
    mother = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                               blank=True, related_name='self_mother')
    spouse = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                               blank=True, related_name='self_spouse')
    sibling_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['house', 'sibling_order']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def is_alive(self):
        return True if not self.is_dead else False

    def has_mother(self):
        return True if self.mother else False

    # Boolean fields
    is_alive.boolean = True


class Alias(TimeStampedModel):
    """Person's aliases

    Person <1:M> Alias
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Alias'
        verbose_name_plural = 'Aliases'

    def __str__(self):
        return self.name


class Title(TimeStampedModel):
    """Person title"""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
