# Generated by Django 3.2.5 on 2021-10-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0036_alter_species_bloom_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='plant_id',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
