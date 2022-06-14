# Generated by Django 3.0.10 on 2020-11-11 20:12

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20201107_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventindexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('green_heading', wagtail.core.blocks.CharBlock(help_text='Green centered text', max_length=200)), ('emphatic_text', home.models.EmphaticText(help_text='Red italic text', required=False)), ('paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('paragraph', wagtail.core.blocks.RichTextBlock())], classname='paragraph', required=True)), ('tan_bg_text', wagtail.core.blocks.RichTextBlock(form_classname='paragraph', help_text='Paragraph with a tan background', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_link_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200, required=False)), ('url', wagtail.core.blocks.URLBlock(label='URL')), ('image', wagtail.images.blocks.ImageChooserBlock())]), label='Image Links'))])), ('html', wagtail.core.blocks.RawHTMLBlock(required=False)), ('image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(help_text='Displayed right of image in h2 tag, centered and uppercase', label='Title', max_length=200)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='Displayed under title, centered and green', label='Subtitle', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Optional text to be displayed alongside image', label='Text', required=False)), ('link_url', wagtail.core.blocks.URLBlock(help_text='If provided, the link will be applied to the image', label='Link URL', max_length=200, required=False))]), help_text='Images displayed with text to the right, all with a tan background', label='List Item'))], required=False)), ('page_link', wagtail.core.blocks.PageChooserBlock())], blank=True),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='body',
            field=wagtail.core.fields.StreamField([('green_heading', wagtail.core.blocks.CharBlock(help_text='Green centered text', max_length=200)), ('emphatic_text', home.models.EmphaticText(help_text='Red italic text', required=False)), ('paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('paragraph', wagtail.core.blocks.RichTextBlock())], classname='paragraph', required=True)), ('tan_bg_text', wagtail.core.blocks.RichTextBlock(form_classname='paragraph', help_text='Paragraph with a tan background', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_link_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200, required=False)), ('url', wagtail.core.blocks.URLBlock(label='URL')), ('image', wagtail.images.blocks.ImageChooserBlock())]), label='Image Links'))])), ('html', wagtail.core.blocks.RawHTMLBlock(required=False)), ('image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(help_text='Displayed right of image in h2 tag, centered and uppercase', label='Title', max_length=200)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='Displayed under title, centered and green', label='Subtitle', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Optional text to be displayed alongside image', label='Text', required=False)), ('link_url', wagtail.core.blocks.URLBlock(help_text='If provided, the link will be applied to the image', label='Link URL', max_length=200, required=False))]), help_text='Images displayed with text to the right, all with a tan background', label='List Item'))], required=False))]),
        ),
    ]
