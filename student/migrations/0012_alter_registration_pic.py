# Generated by Django 4.2.6 on 2024-04-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_registration_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='pic',
            field=models.ImageField(null=True, upload_to='profile_images/'),
        ),
    ]
