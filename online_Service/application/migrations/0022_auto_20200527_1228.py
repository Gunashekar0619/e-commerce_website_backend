# Generated by Django 3.0.6 on 2020-05-27 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0021_goods_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='photo',
        ),
        migrations.AddField(
            model_name='goods',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
