# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 01:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repos', '0004_auto_20170625_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
