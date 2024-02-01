# Generated by Django 4.1.10 on 2024-01-30 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0061_remove_concertdonorclubmember_additional_concerts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concert',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='concert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='year',
        ),
        migrations.AddField(
            model_name='concert',
            name='begin',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 30, 20, 19, 42, 362975, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='concert',
            name='doors_before_event_time_minutes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='concert',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 30, 20, 19, 57, 286010, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='concert',
            name='etix_id',
            field=models.PositiveBigIntegerField(default=1234, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='concert',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
