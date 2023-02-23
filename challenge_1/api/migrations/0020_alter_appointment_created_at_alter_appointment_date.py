# Generated by Django 4.1.7 on 2023-02-23 11:16

import api.models
import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_appointment_created_at_alter_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 2, 23, 12, 16, 27, 312560), default=datetime.datetime(2023, 2, 23, 12, 16, 27, 312560)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[api.models.Appointment.validate_date]),
        ),
    ]
