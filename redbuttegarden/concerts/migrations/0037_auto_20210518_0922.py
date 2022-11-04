# Generated by Django 3.0.10 on 2021-05-18 15:22

import datetime
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0036_auto_20210513_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concertpage',
            name='body',
            field=wagtail.fields.StreamField([('concerts', wagtail.blocks.StructBlock([('band_img', wagtail.images.blocks.ImageChooserBlock(required=True)), ('hidden', wagtail.blocks.BooleanBlock(default=True, help_text='If hidden box is checked, concert will not be displayed on the page', required=False)), ('virtual', wagtail.blocks.BooleanBlock(default=False, help_text='Is this a virtual concert?', required=False)), ('canceled', wagtail.blocks.BooleanBlock(default=False, required=False)), ('postponed', wagtail.blocks.BooleanBlock(default=False, required=False)), ('sold_out', wagtail.blocks.BooleanBlock(default=False, required=False)), ('available_until', wagtail.blocks.DateTimeBlock(blank=True, help_text='Date that on-demand virtual concert will remain available until', null=True, required=False)), ('band_info', wagtail.blocks.RichTextBlock(help_text='Provide the names of the bands/openers and any other info here. Text will be centered.')), ('concert_dates', wagtail.blocks.ListBlock(wagtail.blocks.DateTimeBlock())), ('gates_time', wagtail.blocks.TimeBlock(blank=True, default=datetime.time(18, 0), null=True, required=False)), ('show_time', wagtail.blocks.TimeBlock(blank=True, default=datetime.time(19, 0), null=True, required=False)), ('member_price', wagtail.blocks.CharBlock(blank=True, default='$', max_length=100, null=True)), ('public_price', wagtail.blocks.CharBlock(default='$', max_length=100)), ('ticket_url', wagtail.blocks.URLBlock(default='https://redbuttegarden.ticketfly.com'))]))], blank=True, null=True),
        ),
    ]
