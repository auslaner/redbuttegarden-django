# Generated by Django 4.1.3 on 2023-03-03 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0050_concertpage_wave_one_info_concertpage_wave_two_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='concertpage',
            name='wave_two_sale_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
