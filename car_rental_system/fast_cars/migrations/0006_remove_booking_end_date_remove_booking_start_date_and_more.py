# Generated by Django 4.1.7 on 2023-06-02 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_cars', '0005_remove_booking_timestamp_booking_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
