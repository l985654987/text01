# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-13 08:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190413_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]
