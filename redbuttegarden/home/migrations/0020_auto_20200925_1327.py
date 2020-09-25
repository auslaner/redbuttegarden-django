# Generated by Django 3.0.10 on 2020-09-25 19:27

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200925_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalindexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.RichTextBlock(classname='paragraph', required=True)), ('tan_bg_text', wagtail.core.blocks.RichTextBlock(classname='paragraph', help_text='Paragraph with a tan background', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], label='Info Text'))]), label='Button'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.RichTextBlock(classname='paragraph', required=True)), ('tan_bg_text', wagtail.core.blocks.RichTextBlock(classname='paragraph', help_text='Paragraph with a tan background', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], label='Info Text'))]), label='Button'))])), ('card_info_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], help_text='Note that h4 elements will be colored green and h5 elements will be colored purple', label='Text')), ('button_text', wagtail.core.blocks.CharBlock(label='Button Text')), ('button_url', wagtail.core.blocks.CharBlock(label='Button URL'))]), label='Image Card List Item'))]))]),
        ),
        migrations.AlterField(
            model_name='twocolumngeneralpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))]))], icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))]))], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('html', wagtail.core.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], label='Info Text'))]), label='Button'))]))], blank=True, null=True),
        ),
    ]
