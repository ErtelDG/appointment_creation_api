# Generated by Django 4.1.7 on 2023-02-20 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_appointment_created_at_alter_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='title',
            field=models.CharField(default='No title', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 2, 20, 19, 39, 11, 864239), default=datetime.datetime(2023, 2, 20, 19, 39, 11, 864239)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 19, 39, 11, 864239)),
        ),
    ]
