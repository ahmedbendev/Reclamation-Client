# Generated by Django 2.2 on 2019-04-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190425_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='logement',
            field=models.IntegerField(null=True),
        ),
    ]