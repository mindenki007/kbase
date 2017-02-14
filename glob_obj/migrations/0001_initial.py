# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 15:09
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('eng', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='English version')),
                ('welsh', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Welsh version')),
                ('comments', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Comments')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glob_obj.Category')),
                ('modified_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]