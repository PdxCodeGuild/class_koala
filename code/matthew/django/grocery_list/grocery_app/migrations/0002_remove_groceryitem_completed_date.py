# Generated by Django 2.2.4 on 2019-08-30 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceryitem',
            name='completed_date',
        ),
    ]