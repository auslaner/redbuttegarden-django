# Generated by Django 3.0.10 on 2021-03-11 19:08

import datetime
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0028_auto_20210311_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concertpage',
            name='body',
            field=wagtail.fields.StreamField([('concerts', wagtail.blocks.StructBlock([('band_img', wagtail.images.blocks.ImageChooserBlock(required=True)), ('virtual', wagtail.blocks.BooleanBlock(default=False, help_text='Is this a virtual concert?')), ('canceled', wagtail.blocks.BooleanBlock(default=False)), ('postponed', wagtail.blocks.BooleanBlock(default=False)), ('sold_out', wagtail.blocks.BooleanBlock(default=False)), ('available_until', wagtail.blocks.DateBlock(blank=True, help_text='Date that on-demand virtual concert will remain available until', null=True, required=False)), ('band_info', wagtail.blocks.RichTextBlock(help_text='Provide the names of the bands/openers and any other info here. Text will be centered.')), ('concert_dates', wagtail.blocks.ListBlock(wagtail.blocks.DateTimeBlock())), ('gates_time', wagtail.blocks.TimeBlock(blank=True, default=datetime.time(18, 0), null=True)), ('show_time', wagtail.blocks.TimeBlock(default=datetime.time(19, 0))), ('member_price', wagtail.blocks.CharBlock(blank=True, default='$', max_length=100, null=True)), ('public_price', wagtail.blocks.CharBlock(default='$', max_length=100)), ('ticket_url', wagtail.blocks.URLBlock(default='https://redbuttegarden.ticketfly.com'))]))], blank=True, null=True),
        ),
    ]
