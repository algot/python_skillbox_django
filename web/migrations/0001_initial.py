# Generated by Django 3.0.6 on 2020-05-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
                ('text', models.TextField()),
            ],
        ),
    ]
