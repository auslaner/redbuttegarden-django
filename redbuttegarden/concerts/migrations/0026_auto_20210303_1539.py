# Generated by Django 3.0.10 on 2021-03-03 22:39

import datetime
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0025_auto_20210303_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concertpage',
            name='body',
            field=wagtail.core.fields.StreamField([('concerts', wagtail.core.blocks.StructBlock([('band_img', wagtail.images.blocks.ImageChooserBlock(required=True)), ('virtual', wagtail.core.blocks.BooleanBlock(default=False, help_text='Is this a virtual concert?')), ('canceled', wagtail.core.blocks.BooleanBlock(default=False)), ('postponed', wagtail.core.blocks.BooleanBlock(default=False)), ('sold_out', wagtail.core.blocks.BooleanBlock(default=False)), ('available_until', wagtail.core.blocks.DateBlock(blank=True, help_text='Date that on-demand virtual concert will remain available until', null=True)), ('band_info', wagtail.core.blocks.RichTextBlock(help_text='Provide the names of the bands/openers and any other info here. Text will be centered.')), ('concert_dates', wagtail.core.blocks.ListBlock(wagtail.core.blocks.DateTimeBlock())), ('gates_time', wagtail.core.blocks.TimeBlock(blank=True, default=datetime.time(18, 0), null=True)), ('show_time', wagtail.core.blocks.TimeBlock(default=datetime.time(19, 0))), ('member_price', wagtail.core.blocks.CharBlock(blank=True, default='$', max_length=100, null=True)), ('public_price', wagtail.core.blocks.CharBlock(default='$', max_length=100)), ('ticket_url', wagtail.core.blocks.URLBlock(default='https://redbuttegarden.ticketfly.com'))]))], blank=True, null=True),
        ),
    ]
