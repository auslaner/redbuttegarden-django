# Generated by Django 3.0.10 on 2021-01-15 20:31

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_auto_20210115_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(form_classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.core.blocks.RichTextBlock())], classname='paragraph', required=True)), ('multi_column_paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.core.blocks.ListBlock(wagtail.core.blocks.RichTextBlock())), ('title', wagtail.core.blocks.CharBlock(help_text='Green centered heading above column content', max_length=100, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Centered image')), ('image_carousel', wagtail.core.blocks.StructBlock([('images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))])), ('html', wagtail.core.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], label='Info Text'))]), label='Button'))])), ('card_info_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], help_text='Note that h4 elements will be colored green and h5 elements will be colored purple', label='Text')), ('button_text', wagtail.core.blocks.CharBlock(label='Button Text', required=False)), ('button_url', wagtail.core.blocks.CharBlock(label='Button URL', required=False))]), label='Image Card List Item'))])), ('image_info_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(help_text='Overlayed on image', label='Image Title', max_length=100, required=False)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Overlayed on image below title', label='Image Sub-title', max_length=100, required=False)), ('info_title', wagtail.core.blocks.CharBlock(help_text='Title heading for info displayed to the right of the image', label='Information Title', max_length=500, required=True)), ('info_subtitle', wagtail.core.blocks.CharBlock(help_text='Subheading for info displayed beneath the Information Title', label='Information Sub-title', max_length=500, required=False)), ('tan_bg_info', wagtail.core.blocks.RichTextBlock(help_text='Text is centered, bold and green inside a tan background element', label='Tan background info text')), ('tan_bg_button_text', wagtail.core.blocks.CharBlock(help_text='Text for button within tan background element', label='Button text', required=False)), ('tan_bg_button_url', wagtail.core.blocks.URLBlock(help_text='URL for button', required=False)), ('additional_info', wagtail.core.blocks.RichTextBlock(help_text='Text displayed below tan background element', required=False))]), label='Image Information'))])), ('three_column_dropdown_info_panel', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default-panel', 'Default'), ('purple-panel', 'Purple'), ('orange-panel', 'Orange'), ('blue-panel', 'Blue'), ('green-panel', 'Green')])), ('col_one_header', wagtail.core.blocks.RichTextBlock(help_text='Header for first column of dropdown panel', label='Column One Panel Header', required=True)), ('col_two_header', wagtail.core.blocks.RichTextBlock(help_text='Header for second column of dropdown panel', label='Column Two Panel Header', required=True)), ('col_three_header', wagtail.core.blocks.RichTextBlock(help_text='Header for third column of dropdown panel', label='Column Three Panel Header', required=True)), ('class_info_subheaders', wagtail.core.blocks.BooleanBlock(help_text='Select this option to include class-related subheadings for all columns (e.g. Grade, Ages, Session, Location, Cost', label='Subheaders for Classes')), ('col_one_top_info', wagtail.core.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears after the "GRADE:" subheading')), ('col_two_top_info', wagtail.core.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears after the "AGES:" subheading')), ('col_three_top_info', wagtail.core.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears after the "SESSION:" subheading')), ('middle_info', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.core.blocks.RichTextBlock())], help_text='Text info appearing inside expanded panel between top and bottom subheader content')), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))], required=False)), ('col_one_bottom_info', wagtail.core.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears beside the "LOCATION:" subheading')), ('col_two_bottom_info', wagtail.core.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears beside the "COST:" subheading')), ('col_three_bottom_info', wagtail.core.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears beside the "CONTACT INFORMATION:" subheading'))]), label='Thee Column Dropdown Info Panel'))]))]),
        ),
    ]
