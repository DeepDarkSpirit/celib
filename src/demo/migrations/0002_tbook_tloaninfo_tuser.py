# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('bookid', models.DecimalField(db_column='BOOKID', decimal_places=30, max_digits=65, primary_key=True, serialize=False)),
                ('bookname', models.CharField(db_column='BOOKNAME', max_length=50)),
                ('qty', models.DecimalField(db_column='QTY', decimal_places=30, max_digits=65)),
                ('author', models.CharField(db_column='AUTHOR', max_length=50)),
                ('press', models.CharField(db_column='PRESS', max_length=50)),
                ('state', models.CharField(db_column='STATE', max_length=5)),
                ('createdate', models.DateTimeField(db_column='CREATEDATE')),
                ('creater', models.CharField(db_column='CREATER', max_length=50)),
                ('changedate', models.CharField(blank=True, db_column='CHANGEDATE', max_length=50, null=True)),
                ('changer', models.CharField(blank=True, db_column='CHANGER', max_length=50, null=True)),
            ],
            options={
                'db_table': 't_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TLoaninfo',
            fields=[
                ('loanid', models.DecimalField(db_column='LOANID', decimal_places=30, max_digits=65, primary_key=True, serialize=False)),
                ('fromdate', models.DateTimeField(db_column='FROMDATE')),
                ('todate', models.DateTimeField(db_column='TODATE')),
                ('realdate', models.DateTimeField(blank=True, db_column='REALDATE', null=True)),
                ('remark', models.CharField(blank=True, db_column='REMARK', max_length=200, null=True)),
                ('state', models.CharField(db_column='STATE', max_length=5)),
                ('cretetime', models.CharField(db_column='CRETETIME', max_length=50)),
                ('creater', models.CharField(db_column='CREATER', max_length=50)),
                ('changedate', models.CharField(blank=True, db_column='CHANGEDATE', max_length=50, null=True)),
                ('changer', models.CharField(blank=True, db_column='CHANGER', max_length=50, null=True)),
            ],
            options={
                'db_table': 't_loaninfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('userid', models.DecimalField(db_column='USERID', decimal_places=30, max_digits=65, primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='USERNAME', max_length=50)),
                ('mobile', models.CharField(blank=True, db_column='MOBILE', max_length=20, null=True)),
                ('state', models.CharField(db_column='STATE', max_length=5)),
                ('createdate', models.DateTimeField(db_column='CREATEDATE')),
                ('creater', models.CharField(db_column='CREATER', max_length=50)),
                ('changetime', models.DateTimeField(blank=True, db_column='CHANGETIME', null=True)),
                ('changer', models.CharField(blank=True, db_column='CHANGER', max_length=50, null=True)),
            ],
            options={
                'db_table': 't_user',
                'managed': False,
            },
        ),
    ]
