# Generated by Django 3.0.6 on 2020-05-28 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200528_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
