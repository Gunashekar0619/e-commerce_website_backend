# Generated by Django 3.0.6 on 2020-05-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_userprofile_nameu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nameu',
            field=models.CharField(max_length=20),
        ),
    ]
