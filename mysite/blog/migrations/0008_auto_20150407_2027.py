# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150407_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='hero_image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
