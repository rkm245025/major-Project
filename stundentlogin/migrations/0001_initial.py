# Generated by Django 4.2.6 on 2023-11-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('answerby', models.CharField(max_length=50)),
                ('postedate', models.CharField(max_length=30)),
                ('qid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('postedby', models.CharField(max_length=100)),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StuResponce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('responcetype', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('responcetext', models.CharField(max_length=1000)),
                ('responcedate', models.CharField(max_length=30)),
            ],
        ),
    ]
