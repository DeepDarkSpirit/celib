# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('tel', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cardid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('tel', models.CharField(max_length=45)),
                ('cardid', models.CharField(max_length=45)),
                ('roomtype', models.CharField(choices=[(b'standard', b'\xe6\xa0\x87\xe5\x87\x86\xe9\x97\xb4'), (b'better', b'\xe8\xb1\xaa\xe5\x8d\x8e\xe9\x97\xb4'), (b'president', b'\xe6\x80\xbb\xe7\xbb\x9f\xe9\x97\xb4')], max_length=45)),
                ('begin', models.DateField()),
                ('end', models.DateField()),
                ('totalprice', models.IntegerField()),
                ('state', models.CharField(choices=[(b'will', b'\xe9\xa2\x84\xe5\xae\x9a\xe4\xb8\xad'), (b'run', b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xb8\xad'), (b'end', b'\xe5\xb7\xb2\xe7\xbb\x93\xe6\x9d\x9f'), (b'destroyed', b'\xe5\xb7\xb2\xe5\xba\x9f\xe5\xbc\x83')], max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]