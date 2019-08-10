# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-07-10 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20190709_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', editable=False, help_text='Event Category', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default='', editable=False, help_text='Event Category', on_delete=django.db.models.deletion.CASCADE, to='events.EventCategory'),
        ),
    ]
