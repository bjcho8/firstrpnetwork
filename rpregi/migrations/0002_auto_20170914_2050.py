# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpregi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rplist',
            name='VisualfieldLt',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='rplist',
            name='VisualfieldRt',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='rplist',
            name='fundusLt',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='rplist',
            name='fundusRt',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rplist',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rplist',
            name='sex',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='rplist',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
