# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codeoffapp', '0007_auto_20171028_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_posted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeoffapp.Profile'),
        ),
    ]
