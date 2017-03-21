# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('seen', models.BooleanField(default=False)),
                ('label', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('designee', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
