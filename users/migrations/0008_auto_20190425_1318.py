# Generated by Django 2.2 on 2019-04-25 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_adress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adress',
            new_name='Address',
        ),
    ]
