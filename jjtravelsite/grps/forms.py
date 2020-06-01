from django import forms
from django.contrib.postgres.forms import SplitArrayField

from .models import (GroupName, GroupDetail,)

from people.models import Person

'''
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
'''
'''
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
'''

class GroupNameForm(forms.ModelForm):
    class Meta:
        model = GroupName
        fields = ['departure_date', 'name']


class GroupDetailForm(forms.ModelForm):
    group_name = forms.ModelChoiceField(queryset=GroupName.objects.all(),
                                        empty_label="(Choose Group)")
    tour_guide = forms.ModelChoiceField(queryset=Person.objects.all(),
                                        empty_label='(Choose Person)')
    pax = forms.IntegerField(max_value=100, help_text='Total PAX including Tour Leader')
    is_tour_leader = forms.BooleanField(required=True, label='Tour Leader')
    extra_notes = SplitArrayField(forms.CharField(max_length=100, strip=True),
                                  size=5, remove_trailing_nulls=True)



'''
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
'''
'''
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
'''
