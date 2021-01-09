# Generated by Django 3.0.10 on 2021-01-09 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('concerts', '0009_auto_20201218_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='concertpage',
            name='thumbnail',
            field=models.ForeignKey(blank=True, help_text='You only need to add a thumbnail if this page is the child of a general index page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='donorpackagepage',
            name='thumbnail',
            field=models.ForeignKey(blank=True, help_text='You only need to add a thumbnail if this page is the child of a general index page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
