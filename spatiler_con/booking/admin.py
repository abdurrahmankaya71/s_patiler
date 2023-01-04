from django.contrib import admin
from .models import *

# admin.site.register(Appointment)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','phone','email','service','animal', 'gender', 'day','time','time_ordered')
    list_filter = ('name', 'surname','service',) # filtreleme
    search_fields = ('name', 'surname','phone','email','service','animal', 'gender', 'day','time','time_ordered') # arama

admin.site.register(Appointment, AppointmentAdmin) 
