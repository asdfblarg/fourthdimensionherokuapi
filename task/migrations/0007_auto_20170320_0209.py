# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20170320_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_table',
            name='task_list',
        ),
        migrations.DeleteModel(
            name='Task_Table_List',
        ),
    ]
