# Generated by Django 3.0.10 on 2021-07-14 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0019_auto_20210710_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='genus',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'ordering': ['name'], 'verbose_name_plural': 'species'},
        ),
    ]
