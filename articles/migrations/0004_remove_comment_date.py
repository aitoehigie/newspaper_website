# Generated by Django 3.1.1 on 2020-09-07 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200907_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
    ]