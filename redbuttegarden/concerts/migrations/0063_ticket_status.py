# Generated by Django 4.1.10 on 2024-02-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0062_alter_concert_options_remove_concert_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(blank=True, choices=[('ISSUED', 'Issued'), ('REDEEMED', 'Redeemed')], max_length=20, null=True),
        ),
    ]
