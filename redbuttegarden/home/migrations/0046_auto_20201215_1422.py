# Generated by Django 3.0.10 on 2020-12-15 21:22

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_eventslides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventslides',
            name='text',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=100, null=True),
        ),
    ]
