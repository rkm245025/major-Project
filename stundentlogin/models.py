from django.db import models

# Create your models here.
class StuResponce(models.Model):
    username=models.IntegerField()
    name=models.CharField(max_length=50)
    #program=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    #contactno=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    responcetype=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    responcetext=models.CharField(max_length=1000)
    responcedate=models.CharField(max_length=30)


class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    question=models.CharField(max_length=500)
    postedby=models.CharField(max_length=100)
    posteddate=models.CharField(max_length=30)
       


class Answer(models.Model):
    aid=models.AutoField(primary_key=True)
    answer=models.TextField()
    answerby=models.CharField(max_length=50)
    postedate=models.CharField(max_length=30)
    qid=models.IntegerField()