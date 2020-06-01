from django import forms
from django.contrib.postgres.forms import SplitArrayField
from .models import (Site, SiteVisit,)


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'city']


class SiteVisitForm(forms.ModelForm):
    class Meta:
        model = SiteVisit
        fields = ['site', 'group', 'date', 'arrival_time', 'departure_time',
                  'transportation_mean', 'entrance_fee', 'participating_clients',
                  'extra_notes']

