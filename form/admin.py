from django.contrib import admin
from form.models import ContactFormModel
# from . models olabilir

# Register your models here.
class ContatFromModelAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'message', 'phone_num', 'email')

admin.site.register(ContactFormModel, ContatFromModelAdmin)    
