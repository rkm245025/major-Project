# Generated by Django 4.2.6 on 2023-11-28 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='my_file',
            new_name='myfile',
        ),
    ]