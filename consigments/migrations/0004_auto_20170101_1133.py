# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consigments', '0003_auto_20161231_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consigments',
            name='modified_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='consigments',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]