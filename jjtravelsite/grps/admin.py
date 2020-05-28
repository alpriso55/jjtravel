from django.contrib import admin
from .forms import (PersonForm, RestaurantForm, RestaurantMenuForm,
                    RestaurantReservationForm, HotelForm,
                    HotelRoomReservationForm, HotelDepositForm,
                    HotelReservationForm, SiteForm, SiteVisitForm)
from .models import (JobPosition, Person,
                     Restaurant, RestaurantMenu, RestaurantReservation,
                     GroupName, GroupDetail, Hotel, HotelRoomReservation,
                     HotelDeposit, HotelReservation, Site, SiteVisit)

""" Admin Site Customization """

admin.site.site_header = "JJ-Travel Groups Database"

""" Business Model Registration """

# Create custom models for the admin site
class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

    list_display = ('firstname', 'lastname', 'nickname')


class RestaurantAdmin(admin.ModelAdmin):
    form = RestaurantForm

    list_display = ('name', 'city', 'address')
    list_filter = ('city', )


class RestaurantMenuAdmin(admin.ModelAdmin):
    form = RestaurantMenuForm

    list_display = ('name', 'restaurant', 'cost_per_person')
    list_filter = ('restaurant', 'cost_per_person')


class RestaurantReservationAdmin(admin.ModelAdmin):
    form = RestaurantReservationForm

    list_display = ('reservation_date_time', 'group', 'restaurant_menu')
    list_filter = ('reservation_date_time', 'group')


class HotelAdmin(admin.ModelAdmin):
    form = HotelForm

    list_display = ('name', 'stars', 'city', 'rooms')
    list_filter = ('city', 'stars')


class HotelRoomReservationAdmin(admin.ModelAdmin):
    form = HotelRoomReservationForm

    list_display = ('staying_date', 'hotel_reservation', 'room_type',  
                    'rate_per_room', 'quantity')
    list_filter = ('staying_date', 'hotel_reservation')


class HotelDepositAdmin(admin.ModelAdmin):
    form = HotelDepositForm

    list_display = ('deposit_date', 'hotel_reservation', 'amount')
    list_filter = ('deposit_date', 'hotel_reservation')


class HotelReservationAdmin(admin.ModelAdmin):
    form = HotelReservationForm

    list_display = ('confirmation_date', 'hotel', 'group')
    list_filter = ('confirmation_date', 'hotel', 'group')


class SiteAdmin(admin.ModelAdmin):
    form = SiteForm

    list_display = ('name', 'city')
    list_filter = ('city', )


class SiteVisitAdmin(admin.ModelAdmin):
    form = SiteVisitForm

    list_display = ('date', 'site', 'group', 'transportation_mean', 
                    'entrance_fee')
    list_filter = ('date', 'site', 'group')


# Register your models here.
admin.site.register(JobPosition)
admin.site.register(Person, PersonAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantMenu, RestaurantMenuAdmin)
admin.site.register(RestaurantReservation, RestaurantReservationAdmin)
admin.site.register(GroupName)
admin.site.register(GroupDetail)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelRoomReservation, HotelRoomReservationAdmin)
admin.site.register(HotelDeposit, HotelDepositAdmin)
admin.site.register(HotelReservation, HotelReservationAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(SiteVisit, SiteVisitAdmin)
