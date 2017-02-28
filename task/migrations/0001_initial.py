# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
                ('label', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('designee', models.CharField(blank=True, max_length=50)),
                ('types', models.CharField(choices=[('OTHERS', 'Others'), ('CLEANING', 'Cleaning'), ('COMPUTER', 'Computer Work'), ('DELIVERY', 'Delivery'), ('TRAVEL', 'Travel')], default='OTHERS', max_length=15)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
