from django.forms import ModelForm
from django import forms
from form.models import ContactFormModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['user_name', 'message', 'phone_num', 'email']
