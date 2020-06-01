from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from datetime import date

from grps.models import GroupDetail


class Site(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Name',
                            help_text='Name of the site visited')
    city = models.CharField(max_length=50,
                            verbose_name='City',
                            help_text='Main city where the site is located')

    # Site.site_visit_set()

    @property
    def full_name(self):
        return f'{self.name} ({self.city})'

    class Meta:
        ordering = ['city', 'name']
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.full_name


class SiteVisit(models.Model):
    class TransportatioMean(models.TextChoices):
        BUS = 'BUS', 'Bus'
        FER = 'FER', 'Ferry'
        AIR = 'AIR', 'Airplane'
        TRA = 'TRA', 'Train'
        WAL = 'WAL', 'Walk'
        TEL = 'TEL', 'Teleferik'
        KAT = 'KAT', 'Katamaran'

    site = models.ForeignKey(Site,
                             on_delete=models.CASCADE,
                             verbose_name='Site',
                             help_text='Choose a site from the list')
    group = models.ForeignKey(GroupDetail,
                              on_delete=models.CASCADE,
                              verbose_name='Group',
                              help_text='Choose a group from the list')
    date = models.DateField(default=date.today,
                            verbose_name='Date')
    arrival_time = models.TimeField(null=True, verbose_name='Arrival Time')
    departure_time = models.TimeField(null=True, verbose_name='Departure Time')
    transportation_mean = models.CharField(max_length=3,
                                           choices=TransportatioMean.choices,
                                           default=TransportatioMean.BUS,
                                           verbose_name='Transportation Mean')
    entrance_fee = models.PositiveSmallIntegerField(verbose_name='Entrance Fee')
    participating_clients = models.PositiveSmallIntegerField(
                                     verbose_name='Participating Clients')

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True,
                             verbose_name='Extra Notes')

    @property
    def total_cost(self):
        return self.entrance_fee*self.participating_clients

    @property
    def full_name(self):
        return f'{self.group} visit at {self.site} on {self.date}'

    class Meta:
        ordering = ['site', 'date']
        verbose_name = 'Site Visit'
        verbose_name_plural = 'Site Visits'

    def __str__(self):
        return self.full_name

