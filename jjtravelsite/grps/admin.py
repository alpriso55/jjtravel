from django.contrib import admin

from .forms import (GroupNameForm, GroupDetailForm,)
from .models import (GroupName, GroupDetail,)

from people.models import (JobPosition, Person,)
from people.forms import (JobPositionForm, PersonForm,)

from sites.models import SiteVisit

from hotels.models import HotelReservation

from restaurants.models import RestaurantReservation

""" Admin Site Customization """

admin.site.site_header = "JJ-Travel Admin"
admin.site.site_title = "JJ-Travel Admin"
admin.site.index_title = "JJ-Travel Database Tables"
admin.AdminSite.empty_value_display = '-empty-'


###########################################################
""" Business Model Registration """

# Create custom models for the admin site
'''
class JobPositionAdmin(admin.ModelAdmin):
    form = JobPositionForm
    
    fieldsets = [
        ("Job Position", {'fields': ['title']}),
        ("Description", {'fields': ['description'],
                            'classes': ['collapse']}),
    ]

    class PersonInline(admin.StackedInline):
        model = Person
        extra = 1

    inlines = [PersonInline]

    search_fields = ['title']


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    list_display = ('firstname', 'lastname', 'nickname')

    search_fields = ['nickname']
'''
'''
class RestaurantAdmin(admin.ModelAdmin):
    form = RestaurantForm
    list_display = ['name', 'city']
    
    fieldsets = [
        ("Restaurant Info", {'fields': ['name', 'city', 'address']}),
        ("Contact Details", {'fields': ['phone_list', 'email_list'],
                             'classes': ['collapse']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']}),
    ]
    
    class RestaurantMenuInline(admin.StackedInline):
        model = RestaurantMenu
        extra = 1

    inlines = [RestaurantMenuInline]

    list_filter = ('city', )
    search_fields = ['name', 'city']


class RestaurantMenuAdmin(admin.ModelAdmin):
    form = RestaurantMenuForm
    list_display = ('name', 'restaurant', 'cost_per_person')

    fieldsets = [
        ("General Info", {'fields': ['name', 'restaurant', 'cost_per_person', 'is_tip_included']}),
        ("Menu Details", {'fields': ['is_brerad_included', 
                                     'appetizer_list',
                                     'soup_list',
                                     'salad_list',
                                     'main_dish_list',
                                     'dessert_list',
                                     'drink_list'],
                          'classes': ['collapse']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})   
    ]

    class RestaurantReservationInline(admin.StackedInline):
        model = RestaurantReservation
        extra = 1

    inlines = [RestaurantReservationInline]

    list_filter = ('cost_per_person', )
    search_fields = ['name', 'restaurant']


class RestaurantReservationAdmin(admin.ModelAdmin):
    form = RestaurantReservationForm
    list_display = ('reservation_date_time', 'group', 'restaurant_menu')
    
    fieldsets = [
        ("General Info", {'fields': ['reservation_date_time',
                                     'group',
                                     'restaurant_menu']}),
        ("Cost Details", {'fields': ['total_pax', 'free_pax', 'extra_payment']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})                             
    ]
    
    list_filter = ('reservation_date_time', 'group')
    search_fields = ['group', 'restaurant_menu']
    date_hierarchy = 'reservation_date_time'
'''

class GroupNameAdmin(admin.ModelAdmin):
    form = GroupNameForm
    list_display = ('departure_date', 'name')

    list_filter = ('departure_date', )
    search_fields = ['departure_date', 'name']


class GroupDetailAdmin(admin.ModelAdmin):
    form = GroupDetailForm
    list_display = ('group_name', 'tour_guide', 'pax', 'is_tour_leader')
    
    fieldsets = [
        ("General Info", {'fields': ['group_name',
                                     'tour_guide',
                                     'pax',
                                     'is_tour_leader']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})
    ]

    class RestaurantReservationInline(admin.StackedInline):
        model = RestaurantReservation
        extra = 1
    
    class HotelReservationInline(admin.StackedInline):
        model = HotelReservation
        extra = 1
    
    class SiteVisitInline(admin.StackedInline):
        model = SiteVisit
        extra = 1
    
    inlines = [SiteVisitInline, 
               HotelReservationInline, 
               RestaurantReservationInline]
    
    list_filter = ('group_name', 'tour_guide')
    search_fields = ['group_name', 'tour_guide']
    date_hierarchy = 'group_name__departure_date'


'''
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
'''
'''
class SiteAdmin(admin.ModelAdmin):
    form = SiteForm
    list_display = ('name', 'city')

    fieldsets = [
        (None, {'fields': ['name', 'city']},),
    ]

    class SiteVisitInline(admin.StackedInline):
        model = SiteVisit
        extra = 1
    
    inlines = [SiteVisitInline]
    search_fields = ['name', 'city']
    # list_filter = ('city', )


class SiteVisitAdmin(admin.ModelAdmin):
    form = SiteVisitForm
    list_display = ('date', 'site', 'group', 'transportation_mean', 
                    'entrance_fee')
    
    fieldsets = [
        (None, {'fields': ['site', 'group']}),
        ("Date - Time", {'fields': ['date',
                                    'arrival_time',
                                    'departure_time',
                                    'transportation_mean']}),
        ("Costs", {'fields': ['entrance_fee', 'participating_clients']}),
        ("Extra Notes", {'fields': ['extra_notes'],
                         'classes': ['collapse']})    
    ]
    
    list_filter = ['date']
    search_fields = ['site', 'group', 'transportation_mean']
    date_hierarchy = 'date'
'''

# Register your models here.
'''
admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(Person, PersonAdmin)
'''
'''
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantMenu, RestaurantMenuAdmin)
admin.site.register(RestaurantReservation, RestaurantReservationAdmin)
'''
admin.site.register(GroupName, GroupNameAdmin)
admin.site.register(GroupDetail, GroupDetailAdmin)
'''
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelRoomReservation, HotelRoomReservationAdmin)
admin.site.register(HotelDeposit, HotelDepositAdmin)
admin.site.register(HotelReservation, HotelReservationAdmin)
'''
'''
admin.site.register(Site, SiteAdmin)
admin.site.register(SiteVisit, SiteVisitAdmin)
'''
