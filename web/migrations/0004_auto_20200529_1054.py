# Generated by Django 3.0.6 on 2020-05-29 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='datetime',
            new_name='date',
        ),
    ]
