# Generated by Django 4.1.3 on 2023-02-14 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('journal', '0027_auto_20221104_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalpagetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag'),
        ),
    ]
