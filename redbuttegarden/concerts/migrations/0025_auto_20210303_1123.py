# Generated by Django 3.0.10 on 2021-03-03 18:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0024_auto_20210129_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='concertpage',
            name='body',
            field=wagtail.core.fields.StreamField([('concerts', wagtail.core.blocks.StructBlock([('concert', wagtail.snippets.blocks.SnippetChooserBlock('concerts.Concert')), ('dates', wagtail.core.blocks.ListBlock(wagtail.core.blocks.DateBlock()))]))], blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Concert',
        ),
    ]
