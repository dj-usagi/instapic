# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapic', '0002_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilepic',
            field=models.CharField(default='', max_length=225),
        ),
    ]
