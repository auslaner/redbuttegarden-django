# Generated by Django 3.0.10 on 2021-02-18 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20210121_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]
