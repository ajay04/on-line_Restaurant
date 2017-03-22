# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplementtut', '0002_remove_myregistrationsupplement_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='myregistrationsupplement',
            name='user_type',
            field=models.CharField(choices=[('customer', 'customer'), ('chef', 'chef'), ('manager', 'manager'), ('delivery man', 'delivery man')], default='customer', max_length=20),
        ),
    ]
