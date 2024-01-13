# Generated by Django 4.1.10 on 2024-01-13 18:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('concerts', '0054_concertdonorclubticketsalepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1984), django.core.validators.MaxValueValidator(2099)], verbose_name='year')),
            ],
        ),
        migrations.AlterField(
            model_name='concertdonorclubticketsalepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('text-center', 'Center'), ('right', 'Right')])), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('tan-bg', 'Tan'), ('green-bg', 'Green'), ('dark-tan-bg', 'Dark Tan'), ('white-bg', 'White'), ('red-bg', 'Red'), ('orange-bg', 'Orange')])), ('paragraph', wagtail.blocks.RichTextBlock())], classname='paragraph', required=True))], use_json_field=True),
        ),
        migrations.CreateModel(
            name='ConcertDonorClubPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1984), django.core.validators.MaxValueValidator(2099)], verbose_name='year')),
                ('concerts', models.ManyToManyField(to='concerts.concert')),
            ],
        ),
        migrations.CreateModel(
            name='ConcertDonorClubMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=150)),
                ('additional_concerts', models.ManyToManyField(to='concerts.concert')),
                ('packages', models.ManyToManyField(to='concerts.concertdonorclubpackage')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
