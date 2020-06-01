from django import forms
from django.contrib.postgres.forms import SplitArrayField

from .models import (Restaurant, RestaurantMenu,)

from grps.models import GroupDetail


class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=50, strip=True)
    city = forms.CharField(max_length=50, strip=True)
    address = forms.CharField(max_length=200, strip=True)
    phone_list = SplitArrayField(forms.CharField(max_length=20, strip=True),
                                 size=5, remove_trailing_nulls=True)
    email_list = SplitArrayField(forms.EmailField(max_length=100),
                                 size=5, remove_trailing_nulls=True)

    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)


class RestaurantMenuForm(forms.ModelForm):
    name = forms.CharField(max_length=50, strip=True)
    is_bread_included = forms.BooleanField()
    is_tip_included = forms.BooleanField()
    appetizer_list = SplitArrayField(forms.CharField(max_length=50, strip=True),
                                     size=5, remove_trailing_nulls=True)
    soup_list = SplitArrayField(forms.CharField(max_length=50, strip=True),
                                size=5, remove_trailing_nulls=True)
    salad_list = SplitArrayField(forms.CharField(max_length=50, strip=True),
                                 size=5, remove_trailing_nulls=True)
    main_dish_list = SplitArrayField(forms.CharField(max_length=50, strip=True),
                                     size=5, remove_trailing_nulls=True)
    dessert_list = SplitArrayField(forms.CharField(max_length=50, strip=True),
                                   size=5, remove_trailing_nulls=True)
    drink_list = SplitArrayField(forms.CharField(max_length=50, strip=True),
                                 size=5, remove_trailing_nulls=True)
    cost_per_person = forms.DecimalField(min_value=0.0,
                                         max_value=10000.0,
                                         max_digits=5,
                                         decimal_places=1)
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all(),
                                        empty_label="(Choose Restaurant)")

    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)


class RestaurantReservationForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=GroupDetail.objects.all(),
                                   empty_label="(Choose Group)")
    restaurant_menu = forms.ModelChoiceField(queryset=RestaurantMenu.objects.all(),
                                             empty_label="(Choose Menu)")

    reservation_date_time = forms.DateTimeField()
    total_pax = forms.IntegerField(min_value=0, max_value=100)
    free_pax = forms.IntegerField(min_value=0, max_value=100)
    # is_confirmed = models.BooleanField(default=False)
    extra_cost = forms.DecimalField(min_value=0.0,
                                    max_value=10000.0,
                                    max_digits=5,
                                    decimal_places=1)

    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)
