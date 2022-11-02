# Generated by Django 3.2.9 on 2022-11-02 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('events', '0031_auto_20221101_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventindexpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page. Note that editing an existing document will apply the changes to ALL pages where the document is used', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page. Note that editing an existing document will apply the changes to ALL pages where the document is used', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]
