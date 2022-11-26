from django.db import models


class Book(models.Model):
    startDate = models.DateTimeField()
    finishDate = models.DateTimeField()
    nameSurname = models.CharField(max_length=30)
