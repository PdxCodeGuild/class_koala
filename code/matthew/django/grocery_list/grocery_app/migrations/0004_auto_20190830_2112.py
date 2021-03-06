# Generated by Django 2.2.4 on 2019-08-30 21:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0003_auto_20190830_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 30, 21, 12, 50, 252404, tzinfo=utc), verbose_name='date completed'),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 30, 21, 12, 50, 252361, tzinfo=utc), verbose_name='date created'),
        ),
    ]
