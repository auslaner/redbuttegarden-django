# Generated by Django 3.0.10 on 2021-07-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('plants', '0016_auto_20210710_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='image',
        ),
        migrations.AddField(
            model_name='species',
            name='images',
            field=models.ManyToManyField(to='wagtailimages.Image'),
        ),
    ]
