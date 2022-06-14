# Generated by Django 3.0.10 on 2021-07-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('plants', '0015_remove_collection_planter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='image',
        ),
        migrations.AddField(
            model_name='species',
            name='image',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='_species_image_+', to='wagtailimages.Image'),
        ),
    ]
