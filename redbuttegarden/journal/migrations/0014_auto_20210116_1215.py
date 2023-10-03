# Generated by Django 3.0.10 on 2021-01-16 19:15

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations

import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0013_auto_20210116_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalindexpage',
            name='body',
            field=wagtail.fields.StreamField([('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=100)), ('url', wagtail.blocks.URLBlock()), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('green_heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(help_text='Red italic text', required=False)), ('paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], classname='paragraph', required=True)), ('multi_column_paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock())), ('title', wagtail.blocks.CharBlock(help_text='Green centered heading above column content', max_length=100, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_link_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', max_length=200, required=False)), ('url', wagtail.blocks.URLBlock(label='URL')), ('image', wagtail.images.blocks.ImageChooserBlock())]), label='Image Links'))])), ('html', wagtail.blocks.RawHTMLBlock(required=False)), ('image_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.blocks.CharBlock(help_text='Displayed right of image in h2 tag, centered and uppercase', label='Title', max_length=200)), ('sub_title', wagtail.blocks.CharBlock(help_text='Displayed under title, centered and green', label='Subtitle', max_length=200)), ('text', wagtail.blocks.RichTextBlock(help_text='Optional text to be displayed alongside image', label='Text', required=False)), ('link_url', wagtail.blocks.URLBlock(help_text='If provided, the link will be applied to the image', label='Link URL', max_length=200, required=False))]), help_text='Images displayed with text to the right, all with a tan background', label='List Item'))], required=False)), ('image_row', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('width', wagtail.blocks.IntegerBlock(required=False)), ('height', wagtail.blocks.IntegerBlock(required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journalpage',
            name='body',
            field=wagtail.fields.StreamField([('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=100)), ('url', wagtail.blocks.URLBlock()), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('green_heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(help_text='Red italic text', required=False)), ('paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], classname='paragraph', required=True)), ('multi_column_paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock())), ('title', wagtail.blocks.CharBlock(help_text='Green centered heading above column content', max_length=100, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_link_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', max_length=200, required=False)), ('url', wagtail.blocks.URLBlock(label='URL')), ('image', wagtail.images.blocks.ImageChooserBlock())]), label='Image Links'))])), ('html', wagtail.blocks.RawHTMLBlock(required=False)), ('image_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.blocks.CharBlock(help_text='Displayed right of image in h2 tag, centered and uppercase', label='Title', max_length=200)), ('sub_title', wagtail.blocks.CharBlock(help_text='Displayed under title, centered and green', label='Subtitle', max_length=200)), ('text', wagtail.blocks.RichTextBlock(help_text='Optional text to be displayed alongside image', label='Text', required=False)), ('link_url', wagtail.blocks.URLBlock(help_text='If provided, the link will be applied to the image', label='Link URL', max_length=200, required=False))]), help_text='Images displayed with text to the right, all with a tan background', label='List Item'))], required=False)), ('image_row', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('width', wagtail.blocks.IntegerBlock(required=False)), ('height', wagtail.blocks.IntegerBlock(required=False))]))]),
        ),
    ]
