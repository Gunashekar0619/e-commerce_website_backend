# Generated by Django 3.0.6 on 2020-05-17 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20200517_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='nameu',
            new_name='name',
        ),
    ]
