# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pets',
            field=models.ManyToManyField(related_name='users', to='main_app.Pet'),
        ),
    ]
