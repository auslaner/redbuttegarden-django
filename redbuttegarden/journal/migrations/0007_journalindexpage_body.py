# Generated by Django 3.0.10 on 2020-12-02 17:34

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_auto_20201112_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalindexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=100)), ('url', wagtail.core.blocks.URLBlock()), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('dk-tn', 'Dark Tan'), ('green', 'Green'), ('org', 'Orange'), ('red', 'Red'), ('tan', 'Tan')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('justify', 'Justified'), ('left', 'Left'), ('right', 'Right')]))])), ('green_heading', home.models.Heading(form_classname='full title', help_text='Text will be green and centered')), ('emphatic_text', home.models.EmphaticText(help_text='Red italic text', required=False)), ('paragraph', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.core.blocks.RichTextBlock())], classname='paragraph', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_link_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200, required=False)), ('url', wagtail.core.blocks.URLBlock(label='URL')), ('image', wagtail.images.blocks.ImageChooserBlock())]), label='Image Links'))])), ('html', wagtail.core.blocks.RawHTMLBlock(required=False)), ('image_list', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(help_text='Displayed right of image in h2 tag, centered and uppercase', label='Title', max_length=200)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='Displayed under title, centered and green', label='Subtitle', max_length=200)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Optional text to be displayed alongside image', label='Text', required=False)), ('link_url', wagtail.core.blocks.URLBlock(help_text='If provided, the link will be applied to the image', label='Link URL', max_length=200, required=False))]), help_text='Images displayed with text to the right, all with a tan background', label='List Item'))], required=False))], blank=True, null=True),
        ),
    ]
