# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wordnn.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('labels', wordnn.models.ListField()),
            ],
        ),
        migrations.CreateModel(
            name='WordVec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', wordnn.models.ListField()),
            ],
        ),
    ]
