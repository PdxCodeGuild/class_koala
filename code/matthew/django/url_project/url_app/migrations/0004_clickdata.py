# Generated by Django 2.2.5 on 2019-09-03 21:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0003_urlshortener_long_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=45)),
                ('time', models.DateTimeField(verbose_name=datetime.datetime(2019, 9, 3, 21, 16, 5, 593317, tzinfo=utc))),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url_app.UrlShortener')),
            ],
        ),
    ]