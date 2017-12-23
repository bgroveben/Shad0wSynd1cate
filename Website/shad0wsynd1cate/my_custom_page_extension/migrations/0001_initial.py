# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageFieldExtension',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('background_image', filer.fields.image.FilerImageField(null=True, to=settings.FILER_IMAGE_MODEL, blank=True)),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('public_extension', models.OneToOneField(null=True, related_name='draft_extension', editable=False, to='my_custom_page_extension.PageFieldExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
