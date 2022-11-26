from django.db import models

# Create your models here.

class ContactFormModel(models.Model):
    user_name = models.CharField(max_length=50, verbose_name="Ad Soyad")
    email = models.CharField(max_length=50, verbose_name="Email")
    message = models.CharField(max_length=200, verbose_name="Mesaj")
    phone_num = models.CharField(max_length=11, verbose_name="Telefon Numarası")
    
    def __str__(self):
        return self.user_name