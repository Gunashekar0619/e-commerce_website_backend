# Generated by Django 3.0.6 on 2020-05-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0016_remove_userprofile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_id',
        ),
    ]
