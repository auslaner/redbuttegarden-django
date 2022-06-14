# Generated by Django 3.0.10 on 2021-01-19 20:34

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20210115_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twocolumngeneralpage',
            name='body',
            field=wagtail.core.fields.StreamField([('green_heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(form_classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(form_classname='full title', help_text='Text will be red, italic and centered')), ('aligned_paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(form_classname='full title', help_text='Text will be red, italic and centered')), ('aligned_paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('html', wagtail.core.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], label='Info Text'))]), label='Button'))]))], blank=True, null=True),
        ),
    ]
