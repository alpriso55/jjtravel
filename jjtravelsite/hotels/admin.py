from django.contrib import admin

from .forms import (HotelForm, HotelDepositForm, HotelReservationForm,
                    HotelRoomReservationForm,)
from .models import (Hotel, HotelDeposit, HotelReservation, HotelRoomReservation,)

###########################################################
""" Business Model Registration """

class HotelAdmin(admin.ModelAdmin):
    form = HotelForm
    list_display = ('name', 'stars', 'city', 'rooms')
    
    fieldsets = [
        ("General Info", {'fields': ['name', 'stars', 'city']}),
        ("Facilities", {'fields': ['rooms', 'floors', 'elevators']}),
        ("Contact Details", {'fields': ['address', 'phone_list', 'email_list']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})
    ]

    class HotelReservationInline(admin.StackedInline):
        model = HotelReservation
        extra = 1
    
    inlines = [HotelReservationInline]
    search_fields = ['name', 'stars', 'city', 'elevators']
    list_filter = ('stars', 'rooms', 'floors')


class HotelReservationAdmin(admin.ModelAdmin):
    form = HotelReservationForm
    list_display = ('confirmation_date', 'hotel', 'group')
    
    fieldsets = [
        (None, {'fields': ['group', 'hotel', 'confirmation_date']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})
    ]

    class HotelDepositInline(admin.StackedInline):
        model = HotelDeposit
        extra = 1
    
    class HotelRoomReservationInline(admin.StackedInline):
        model = HotelRoomReservation
        extra = 1
    
    inlines = [HotelDepositInline, HotelRoomReservationInline]
    
    list_filter = ('confirmation_date', )
    search_fields = ['hotel', 'group']
    date_hierarchy = 'confirmation_date'


class HotelDepositAdmin(admin.ModelAdmin):
    form = HotelDepositForm
    list_display = ('deposit_date', 'hotel_reservation', 'amount')
    
    fieldsets = [
        (None, {'fields': ['deposit_date',
                           'hotel_reservation'
                           'amount']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})
    ]

    list_filter = ['deposit_date', 'amount']
    search_fields = ['hotel_reservation']
    date_hierarchy = 'deposit_date'


class HotelRoomReservationAdmin(admin.ModelAdmin):
    form = HotelRoomReservationForm
    list_display = ('staying_date', 'hotel_reservation', 'room_type',  
                    'rate_per_room', 'quantity')

    fieldsets = [
        (None, {'fields': ['hotel_reservation']}),
        ("Reservation Details", {'fields': ['staying_date',
                                            'room_type',
                                            'meal_plan']}),
        ("Reservation Cost", {'fields': ['rate_per_room', 'quantity']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})
    ]

    list_filter = ['staying_date']
    search_fields = ['hotel_reservation', 'room_type', 'meal_plan']
    date_hierarchy = 'staying_date'


# Register your models here.
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelRoomReservation, HotelRoomReservationAdmin)
admin.site.register(HotelDeposit, HotelDepositAdmin)
admin.site.register(HotelReservation, HotelReservationAdmin)
