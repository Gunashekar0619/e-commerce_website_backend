# Generated by Django 3.0.6 on 2020-05-19 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_remove_userprofile_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
