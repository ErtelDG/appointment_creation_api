# Generated by Django 4.1.7 on 2023-02-20 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 2, 20, 13, 18, 12, 932765), default=datetime.datetime(2023, 2, 20, 13, 18, 12, 932765)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 13, 18, 12, 932765)),
        ),
    ]
