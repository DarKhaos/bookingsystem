# Generated by Django 3.2.5 on 2022-01-23 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 17, 19, 18, 255390)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dni',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 17, 19, 18, 256392)),
        ),
    ]
