# Generated by Django 3.2.5 on 2021-09-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0028_auto_20210715_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciesimage',
            name='copyright',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
