from django import forms
from django.contrib.postgres.forms import SplitArrayField
from .models import (JobPosition, Person,)


class JobPositionForm(forms.ModelForm):
    title = forms.CharField(max_length=50, strip=True)
    description = forms.CharField(max_length=200, strip=True)


class PersonForm(forms.ModelForm):
    firstname = forms.CharField(max_length=20, strip=True)
    lastname = forms.CharField(max_length=20, strip=True)
    nickname = forms.CharField(max_length=20, strip=True,
                               help_text="English name for Korean guides")
    phone_list = SplitArrayField(forms.CharField(max_length=20, strip=True),
                                 size=5, remove_trailing_nulls=True)
    email_list = SplitArrayField(forms.EmailField(max_length=100),
                                 size=5, remove_trailing_nulls=True)
    job_position = forms.ModelChoiceField(queryset=JobPosition.objects.all(),
                                          empty_label=None)
    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)

