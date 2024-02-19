from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Aşlar ve Takibi","Aşlar ve Takibi"),
    ("Doğum ve Jinekoloji Hizmetleri", "Doğum ve Jinekoloji Hizmetleri"),
    ("Cerrahi Operasyonlar", "Cerrahi Operasyonlar"),
    ("Parazit Tedavisi", "Parazit Tedavisi"),
    ("Röntgen/Ultrason", "Röntgen/Ultrason"),
    ("Diş ve Dişeti Tedavisi", "Diş ve Dişeti Tedavisi"),

    )
TIME_CHOICES = (
    ("09:00 - 10:00", "09:00 - 10:00"),
    ("10:00 - 11:00", "10:00 - 11:00"),
    ("11:00 - 12:00", "11:00 - 12:00"),
    ("12:00 - 13:00", "12:00 - 13:00"),
    ("13:00 - 14:00", "13:00 - 14:00"),
    ("14:00 - 15:00", "14:00 - 15:00"),
    ("15:00 - 16:00", "15:00 - 16:00"),
    ("16:00 - 17:00", "16:00 - 17:00"),
    ("17:00 - 18:00", "17:00 - 18:00"),
)

GENDER_CHOICES = (
    ("Erkek", "Erkek"),
    ("Dişi", "Dişi"),
)

ANIMAL_CHOICES = (
    ("Kedi", "Kedi"),
    ("Köpek", "Köpek"),
    ("Kuş", "Kuş"),
    ("Diğer", "Diğer"),
)

class Appointment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50,verbose_name="Ad")
    surname = models.CharField(max_length=50,verbose_name="Soyad")
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Aşlar ve Takibi", verbose_name="Hizmet")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=50, choices=TIME_CHOICES, default="3 PM", verbose_name="Saat")
    phone = models.CharField(max_length=11, verbose_name="Telefon Numarası")
    email = models.CharField(max_length=50, verbose_name="Email")
    animal = models.CharField(max_length=50, choices= ANIMAL_CHOICES, default="Kedi", verbose_name="Hayvan")
    gender = models.CharField(max_length=50, choices= GENDER_CHOICES, default="Erkek", verbose_name="Cinsiyet")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Randevu Alma Saati")
    def __str__(self):
        return f"{self.name} | Randevu Günü: {self.day} | Randevu Saati: {self.time}"
    
    class Meta:
        verbose_name = "Randevu"
        verbose_name_plural = "Randevular"
        

