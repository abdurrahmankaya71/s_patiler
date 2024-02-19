# Generated by Django 4.1.3 on 2022-11-30 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_rename_hayvan_appointment_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.CharField(default=datetime.datetime(2022, 11, 30, 20, 53, 5, 985951), max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone',
            field=models.CharField(default=datetime.datetime(2022, 11, 30, 20, 54, 6, 445970), max_length=11, verbose_name='Telefon Numarası'),
            preserve_default=False,
        ),
    ]