# Generated by Django 3.0.6 on 2020-06-21 04:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0024_auto_20200614_0928'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='goods',
            unique_together={('name', 'owner')},
        ),
    ]
