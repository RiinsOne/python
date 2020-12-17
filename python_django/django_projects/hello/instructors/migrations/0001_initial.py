# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-07-17 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='This is name', max_length=255, verbose_name='Instructor name')),
                ('surname', models.CharField(max_length=64)),
                ('data_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('course', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructors.Position'),
        ),
    ]