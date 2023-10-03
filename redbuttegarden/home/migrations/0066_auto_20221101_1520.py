# Generated by Django 3.2.9 on 2022-11-01 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('home', '0065_auto_20210526_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='generalindexpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='generalpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='plantcollectionspage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='retailpartnerpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AddField(
            model_name='twocolumngeneralpage',
            name='custom_css',
            field=models.ForeignKey(blank=True, help_text='Upload a CSS file to apply custom styling to this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]
