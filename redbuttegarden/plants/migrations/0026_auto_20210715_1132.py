# Generated by Django 3.0.10 on 2021-07-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0025_auto_20210714_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardenarea',
            name='code',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
