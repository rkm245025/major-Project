# Generated by Django 4.2.6 on 2023-11-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_login_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=64)),
                ('enquirytext', models.TextField()),
                ('enquirydate', models.DateField()),
            ],
        ),
    ]