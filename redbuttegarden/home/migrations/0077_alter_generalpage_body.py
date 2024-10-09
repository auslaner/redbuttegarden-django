# Generated by Django 4.2.13 on 2024-07-06 18:33

from django.db import migrations
import home.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_alter_generalindexpage_body_alter_generalpage_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.fields.StreamField([('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=100)), ('url', wagtail.blocks.URLBlock()), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('orange', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('custom_heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('heading_size', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Size')), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')], label='Alignment')), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('orange', 'Orange'), ('red', 'Red'), ('tan', 'Tan')], label='Color')), ('anchor_id', wagtail.blocks.CharBlock(label='Optional Anchor Identifier', required=False))])), ('heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(form_classname='full title', help_text='Text will be red, italic and centered')), ('paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], classname='paragraph', required=True)), ('multi_column_paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock())), ('title', wagtail.blocks.CharBlock(help_text='Green centered heading above column content', max_length=100, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Centered image')), ('image_carousel', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))])), ('html', wagtail.blocks.RawHTMLBlock()), ('dropdown_image_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.blocks.RichTextBlock(label='Text'))]), label='List Item'))])), ('dropdown_button_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(label='Button Text', max_length=200)), ('info_text', wagtail.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'document-link', 'ul'], label='Info Text'))]), label='Button'))])), ('dropdown_card_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('card_info', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], label='Card Text')), ('info_text', wagtail.blocks.RichTextBlock(label='Info Text')), ('info_button_text', wagtail.blocks.CharBlock(help_text='Button appears below Info Text', max_length=100, required=False)), ('info_button_url', wagtail.blocks.URLBlock(label='Button URL', max_length=200, required=False))]), label='Card'))])), ('card_info_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('text', wagtail.blocks.RichTextBlock(features=['h4', 'h5', 'bold', 'italic', 'link', 'ul'], help_text='Note that h4 elements will be colored green and h5 elements will be colored purple', label='Text')), ('button_text', wagtail.blocks.CharBlock(label='Button Text', required=False)), ('button_url', wagtail.blocks.CharBlock(label='Button URL', required=False))]), label='Image Card List Item'))])), ('image_info_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(help_text='Overlayed on image', label='Image Title', max_length=100, required=False)), ('subtitle', wagtail.blocks.CharBlock(help_text='Overlayed on image below title', label='Image Sub-title', max_length=100, required=False)), ('info_title', wagtail.blocks.CharBlock(help_text='Title heading for info displayed to the right of the image', label='Information Title', max_length=500, required=True)), ('info_subtitle', wagtail.blocks.CharBlock(help_text='Subheading for info displayed beneath the Information Title', label='Information Sub-title', max_length=500, required=False)), ('tan_bg_info', wagtail.blocks.RichTextBlock(help_text='Text is centered, bold and green inside a tan background element', label='Tan background info text')), ('tan_bg_button_text', wagtail.blocks.CharBlock(help_text='Text for button within tan background element', label='Button text', required=False)), ('tan_bg_button_url', wagtail.blocks.URLBlock(help_text='URL for button', required=False)), ('additional_info', wagtail.blocks.RichTextBlock(help_text='Text displayed below tan background element', required=False))]), label='Image Information'))])), ('image_link_list', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', max_length=200, required=False)), ('url', wagtail.blocks.URLBlock(label='URL')), ('image', wagtail.images.blocks.ImageChooserBlock())]), label='Image Links'))])), ('three_column_dropdown_info_panel', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('background_color', wagtail.blocks.ChoiceBlock(choices=[('default-panel', 'Default'), ('purple-panel', 'Purple'), ('orange-panel', 'Orange'), ('blue-panel', 'Blue'), ('green-panel', 'Green')])), ('col_one_header', wagtail.blocks.RichTextBlock(help_text='Header for first column of dropdown panel', label='Column One Panel Header', required=True)), ('col_two_header', wagtail.blocks.RichTextBlock(help_text='Header for second column of dropdown panel', label='Column Two Panel Header', required=True)), ('col_three_header', wagtail.blocks.RichTextBlock(help_text='Header for third column of dropdown panel', label='Column Three Panel Header', required=True)), ('class_info_subheaders', wagtail.blocks.BooleanBlock(help_text='Select this option to include class-related subheadings for all columns (e.g. Grade, Ages, Session, Location, Cost', label='Subheaders for Classes')), ('col_one_top_info', wagtail.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears after the "GRADE:" subheading')), ('col_two_top_info', wagtail.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears after the "AGES:" subheading')), ('col_three_top_info', wagtail.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears after the "SESSION:" subheading')), ('middle_info', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], help_text='Text info appearing inside expanded panel between top and bottom subheader content')), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=100)), ('url', wagtail.blocks.URLBlock()), ('color', wagtail.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('orange', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))], required=False)), ('col_one_bottom_info', wagtail.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears beside the "LOCATION:" subheading')), ('col_two_bottom_info', wagtail.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears beside the "COST:" subheading')), ('col_three_bottom_info', wagtail.blocks.RichTextBlock(help_text='If class subheaders are selected, this text appears beside the "CONTACT INFORMATION:" subheading'))]), label='Thee Column Dropdown Info Panel'))])), ('newsletters', wagtail.blocks.StructBlock([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=100, required=False)), ('embed', wagtail.blocks.RawHTMLBlock(required=True))])))]))], use_json_field=True),
        ),
    ]
