# Generated by Django 3.0.10 on 2021-01-12 22:10

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0015_auto_20210112_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concert',
            name='band_name',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='band_url',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='opener_name',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='opener_url',
        ),
        migrations.AddField(
            model_name='concert',
            name='band_info',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
