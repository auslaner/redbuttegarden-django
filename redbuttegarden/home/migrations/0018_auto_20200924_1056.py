# Generated by Django 3.0.10 on 2020-09-24 16:56

from django.db import migrations
import home.models
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200924_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalindexpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.RichTextBlock(classname='paragraph', required=True)), ('tan_bg_text', wagtail.blocks.RichTextBlock(classname='paragraph', help_text='Paragraph with a tan background', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.blocks.RichTextBlock(label='Info Text'))]), label='Button'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.fields.StreamField([('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=100)), ('url', wagtail.blocks.URLBlock()), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.RichTextBlock(classname='paragraph', required=True)), ('tan_bg_text', wagtail.blocks.RichTextBlock(classname='paragraph', help_text='Paragraph with a tan background', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.blocks.RichTextBlock(label='Info Text'))]), label='Button'))]))]),
        ),
        migrations.AlterField(
            model_name='twocolumngeneralpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('two_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StreamBlock([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=100)), ('url', wagtail.blocks.URLBlock()), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))]))], icon='arrow-left', label='Left column content')), ('right_column', wagtail.blocks.StreamBlock([('heading', home.models.Heading(classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=100)), ('url', wagtail.blocks.URLBlock()), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))]))], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('html', wagtail.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.blocks.RichTextBlock(label='Info Text'))]), label='Button'))]))], blank=True, null=True),
        ),
    ]
