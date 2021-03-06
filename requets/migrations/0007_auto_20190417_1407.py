# Generated by Django 2.2 on 2019-04-17 12:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requets', '0006_auto_20190417_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='requet',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 12, 7, 23, 625362, tzinfo=utc)),
        ),
    ]
