# Generated by Django 4.1.10 on 2024-02-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0065_alter_concertdonorclubmember_packages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concertdonorclubmember',
            name='packages',
            field=models.ManyToManyField(blank=True, to='concerts.concertdonorclubpackage'),
        ),
        migrations.AlterField(
            model_name='concertdonorclubpackage',
            name='concerts',
            field=models.ManyToManyField(blank=True, to='concerts.concert'),
        ),
    ]
