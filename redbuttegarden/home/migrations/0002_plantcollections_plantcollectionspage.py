# Generated by Django 3.0.3 on 2020-03-11 17:15

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantCollectionsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField()),
                ('more_info_modal', wagtail.core.fields.RichTextField()),
                ('banner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('collection_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PlantCollections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('text', wagtail.core.fields.RichTextField()),
                ('slideshow_link', models.URLField()),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plant_collections', to='home.PlantCollectionsPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
