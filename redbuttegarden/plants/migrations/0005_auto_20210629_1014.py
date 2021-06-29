# Generated by Django 3.0.10 on 2021-06-29 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_auto_20210629_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
