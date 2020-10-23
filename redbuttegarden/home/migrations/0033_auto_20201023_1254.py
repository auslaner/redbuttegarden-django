# Generated by Django 3.0.10 on 2020-10-23 18:54

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20201010_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalindexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('paragraph', wagtail.core.blocks.RichTextBlock())], classname='paragraph', required=True)), ('tan_bg_text', wagtail.core.blocks.RichTextBlock(classname='paragraph', help_text='Paragraph with a tan background', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], label='Info Text'))]), label='Button'))])), ('image_link_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('url', wagtail.core.blocks.URLBlock(label='URL')), ('image', wagtail.images.blocks.ImageChooserBlock())]), label='Image Links'))]))], blank=True),
        ),
    ]
