# Generated by Django 3.0.10 on 2021-01-12 23:00

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0016_auto_20210112_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='virtual',
            field=models.BooleanField(default=False, help_text='Is this a virtual concert?'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='band_info',
            field=wagtail.core.fields.RichTextField(help_text='Provide the names of the bands/openers and any other info here. Text will be centered.'),
        ),
    ]
