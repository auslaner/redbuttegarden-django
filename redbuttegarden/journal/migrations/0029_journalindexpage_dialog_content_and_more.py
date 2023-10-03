# Generated by Django 4.1.3 on 2023-01-20 22:25

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0028_alter_journalpagetag_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalindexpage',
            name='dialog_content',
            field=wagtail.fields.RichTextField(blank=True, help_text='Main content of the dialog box', null=True),
        ),
        migrations.AddField(
            model_name='journalindexpage',
            name='dialog_display',
            field=models.BooleanField(blank=True, help_text='Should this dialog be displayed?', null=True),
        ),
        migrations.AddField(
            model_name='journalindexpage',
            name='dialog_style',
            field=models.CharField(blank=True, choices=[('corner', 'Corner'), ('full', 'Full Page')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='journalindexpage',
            name='dialog_title',
            field=models.CharField(blank=True, help_text='Title for pop-up dialog box', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='journalpage',
            name='dialog_content',
            field=wagtail.fields.RichTextField(blank=True, help_text='Main content of the dialog box', null=True),
        ),
        migrations.AddField(
            model_name='journalpage',
            name='dialog_display',
            field=models.BooleanField(blank=True, help_text='Should this dialog be displayed?', null=True),
        ),
        migrations.AddField(
            model_name='journalpage',
            name='dialog_style',
            field=models.CharField(blank=True, choices=[('corner', 'Corner'), ('full', 'Full Page')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='journalpage',
            name='dialog_title',
            field=models.CharField(blank=True, help_text='Title for pop-up dialog box', max_length=100, null=True),
        ),
    ]
