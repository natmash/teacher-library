# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('times_checked_out', models.IntegerField(default=0, editable=False)),
                ('available', models.BooleanField(default=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now=True)),
                ('end', models.DateTimeField(blank=True, editable=False, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeacherLibrary.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('total_checkouts', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='checkout',
            name='student',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='TeacherLibrary.Student'),
        ),
    ]