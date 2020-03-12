# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-29 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20200111_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default='', help_text='Event Category', on_delete=django.db.models.deletion.CASCADE, to='events.EventCategory'),
        ),
        migrations.AlterField(
            model_name='eventcategory',
            name='category',
            field=models.CharField(default='', help_text='Event Category', max_length=50),
        ),
    ]