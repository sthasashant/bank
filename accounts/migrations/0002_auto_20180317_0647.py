# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 06:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_no',
            field=models.PositiveIntegerField(null=True, unique=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
