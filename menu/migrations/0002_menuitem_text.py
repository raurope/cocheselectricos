# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='text',
            field=models.TextField(default='menu option', help_text='Set the text that will be shown in your menu', verbose_name='Menu option text'),
        ),
    ]
