# Generated by Django 4.1.7 on 2023-02-23 12:15

import api.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_appointment_created_at_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 2, 23, 13, 15, 53, 189737), default=datetime.datetime(2023, 2, 23, 13, 15, 53, 189737)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 13, 15, 53, 189737), validators=[api.models.Appointment.validate_date]),
        ),
    ]
