# Generated by Django 4.2.6 on 2023-11-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=64)),
                ('program', models.CharField(max_length=64)),
                ('branch', models.CharField(max_length=64)),
                ('year', models.CharField(max_length=64)),
                ('subject', models.CharField(max_length=64)),
                ('file_name', models.CharField(max_length=64)),
                ('my_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('newstext', models.TextField()),
                ('newsdate', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=64)),
            ],
        ),
    ]
