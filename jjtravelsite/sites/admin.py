from django.contrib import admin

from .models import (Site, SiteVisit,)
from .forms import (SiteForm, SiteVisitForm,)


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


# Register your models here.
admin.site.register(Site, SiteAdmin)
admin.site.register(SiteVisit, SiteVisitAdmin)
