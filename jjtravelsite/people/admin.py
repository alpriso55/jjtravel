from django.contrib import admin

from .forms import (JobPositionForm, PersonForm,)
from .models import (JobPosition, Person,)

###########################################################
""" Business Model Registration """

# Create custom models for the admin site
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


# Register your models here.
admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(Person, PersonAdmin)
