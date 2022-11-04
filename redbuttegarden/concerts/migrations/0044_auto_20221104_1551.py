# Generated by Django 3.2.16 on 2022-11-04 21:51

import datetime
from django.db import migrations
import home.models
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0043_auto_20221102_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concertpage',
            name='body',
            field=wagtail.fields.StreamField([('concerts', wagtail.blocks.StructBlock([('band_img', wagtail.images.blocks.ImageChooserBlock(required=True)), ('hidden', wagtail.blocks.BooleanBlock(default=True, help_text='If hidden box is checked, concert will not be displayed on the page', required=False)), ('on_sale', wagtail.blocks.BooleanBlock(default=True, help_text='If unchecked, Buy Tickets button will be grayed out', required=False)), ('virtual', wagtail.blocks.BooleanBlock(default=False, help_text='Is this a virtual concert?', required=False)), ('canceled', wagtail.blocks.BooleanBlock(default=False, required=False)), ('postponed', wagtail.blocks.BooleanBlock(default=False, required=False)), ('sold_out', wagtail.blocks.BooleanBlock(default=False, required=False)), ('available_until', wagtail.blocks.DateTimeBlock(blank=True, help_text='Date that on-demand virtual concert will remain available until', null=True, required=False)), ('band_info', wagtail.blocks.RichTextBlock(help_text='Provide the names of the bands/openers and any other info here. Text will be centered.')), ('concert_dates', wagtail.blocks.ListBlock(wagtail.blocks.DateTimeBlock())), ('gates_time', wagtail.blocks.TimeBlock(blank=True, default=datetime.time(18, 0), null=True, required=False)), ('show_time', wagtail.blocks.TimeBlock(blank=True, default=datetime.time(19, 0), null=True, required=False)), ('member_price', wagtail.blocks.CharBlock(blank=True, default='$', max_length=100, null=True)), ('public_price', wagtail.blocks.CharBlock(default='$', max_length=100)), ('ticket_url', wagtail.blocks.URLBlock(default='https://redbuttegarden.ticketfly.com'))]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='donorpackagepage',
            name='body',
            field=wagtail.fields.StreamField([('heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(form_classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], classname='paragraph', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.blocks.RawHTMLBlock()), ('sponsor_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('sponsor_title', wagtail.blocks.CharBlock(label='Sponsor Title', max_length=200, required=False)), ('sponsor_url', wagtail.blocks.URLBlock(label='URL to sponsor website')), ('sponsor_logo', wagtail.images.blocks.ImageChooserBlock())]), label='Sponsors'))])), ('button_table', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(label='Button text')), ('table_list', wagtail.blocks.StreamBlock([('title', home.models.Heading()), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right-click to add/remove rows/columns', table_options={'autoColumnSize': False, 'colHeaders': True, 'editor': 'text', 'height': 216, 'language': 'en-US', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 6, 'startRows': 3, 'stretchH': 'all'}))]))])), ('table_cards', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('body', wagtail.blocks.StreamBlock([('heading', home.models.Heading()), ('paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())])), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'autoColumnSize': False, 'colHeaders': True, 'editor': 'text', 'height': 216, 'language': 'en-US', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 2, 'stretchH': 'all'}))]))]), label='List of info cards with tables'))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right-click to add/remove rows/columns', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo', '---------', 'copy', 'cut---------', 'alignment'], 'editor': 'text', 'height': 216, 'language': 'en-US', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 3, 'stretchH': 'all'}))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='donorschedulepage',
            name='body',
            field=wagtail.fields.StreamField([('heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(form_classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], classname='paragraph', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.blocks.RawHTMLBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right-click to add/remove rows/columns', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo', '---------', 'copy', 'cut---------', 'alignment'], 'editor': 'text', 'height': 216, 'language': 'en-US', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 3, 'stretchH': 'all'})), ('concerts', wagtail.blocks.StreamBlock([('concerts', wagtail.blocks.StructBlock([('band_img', wagtail.images.blocks.ImageChooserBlock(required=True)), ('concert_dates', wagtail.blocks.ListBlock(wagtail.blocks.DateTimeBlock())), ('band_info', wagtail.blocks.RichTextBlock(help_text='Provide the names of the bands/openers and any other info here. Text will be centered.'))]))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='pastconcertpage',
            name='lineups',
            field=wagtail.fields.StreamField([('lineup', wagtail.blocks.StructBlock([('year', wagtail.blocks.IntegerBlock(min_value=1980, required=True)), ('poster', wagtail.images.blocks.ImageChooserBlock(required=True)), ('artists', wagtail.blocks.RichTextBlock(required=True))]))], use_json_field=True),
        ),
    ]
