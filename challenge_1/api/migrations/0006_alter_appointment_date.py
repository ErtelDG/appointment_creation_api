# Generated by Django 4.1.7 on 2023-02-20 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 13, 16, 50, 939660)),
        ),
    ]
