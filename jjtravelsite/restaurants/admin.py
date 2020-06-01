from django.contrib import admin

from .models import (Restaurant, RestaurantMenu, RestaurantReservation,)
from .forms import (RestaurantForm, RestaurantMenuForm, RestaurantReservationForm) 

###########################################################
""" Business Model Registration """


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

# Register your models here.

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantMenu, RestaurantMenuAdmin)
admin.site.register(RestaurantReservation, RestaurantReservationAdmin)
