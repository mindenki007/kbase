# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 15:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170126_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cir',
            name='allocated_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
