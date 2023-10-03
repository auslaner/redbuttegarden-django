# Generated by Django 3.2.9 on 2022-11-01 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('concerts', '0040_alter_donorpackagepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='concertpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='donorpackagepage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='donorschedulepage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='pastconcertpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]
