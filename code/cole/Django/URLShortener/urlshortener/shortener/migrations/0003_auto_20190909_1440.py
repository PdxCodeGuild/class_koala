# Generated by Django 2.2.5 on 2019-09-09 21:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20190909_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 21, 40, 57, 798341, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='url',
            name='urlcode',
            field=models.CharField(default='', max_length=6),
        ),
    ]
