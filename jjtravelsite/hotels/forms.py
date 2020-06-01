from django import forms
from django.contrib.postgres.forms import SplitArrayField

from .models import (Hotel, HotelDeposit, HotelReservation, HotelRoomReservation,)

from grps.models import GroupDetail


class HotelForm(forms.ModelForm):
    """ This is another way for defining a Form based on a Model """
    # class Meta:
    #     model = Hotel
    #     fields = ['name', 'city', 'stars', 'rooms', 'floors',
    #               'elevators', 'address', 'phone_list',
    #               'email_list', 'extra_notes']

    name = forms.CharField(max_length=50, strip=True)
    city = forms.CharField(max_length=50, strip=True)
    stars = forms.IntegerField()
    rooms = forms.IntegerField()
    floors = forms.IntegerField()
    elevators = forms.IntegerField()
    address = forms.CharField(max_length=200, strip=True)
    phone_list = SplitArrayField(forms.CharField(max_length=20, strip=True),
                                 size=5, remove_trailing_nulls=True)
    email_list = SplitArrayField(forms.EmailField(max_length=100),
                                 size=5, remove_trailing_nulls=True)

    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)


class HotelReservationForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=GroupDetail.objects.all(),
                                   empty_label="(Choose Group)")
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(),
                                   empty_label='(Choose Hotel)')
    confirmation_date = forms.DateField()

    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)

    # HotelReservation.hotel_deposit_set()
    # HotelReservation.hotel_room_reservation_set()


class HotelDepositForm(forms.ModelForm):
    deposit_date = forms.DateField()
    amount = forms.DecimalField(max_digits=5,
                                decimal_places=1)
    hotel_reservation = forms.ModelChoiceField(HotelReservation.objects.all(),
                                               empty_label='(Choose Reservation)',
                                               limit_choices_to=20)

    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)


class HotelRoomReservationForm(forms.ModelForm):
    class Meta:
        model = HotelRoomReservation
        fields = ['hotel_reservation', 'room_type', 'meal_plan', 'staying_date',
                  'rate_per_room', 'quantity', 'extra_notes']
