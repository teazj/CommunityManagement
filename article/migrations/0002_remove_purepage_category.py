# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purepage',
            name='category',
        ),
    ]
