from django.db import models

# Create your models here.
class Program(models.Model):
   program=models.CharField(max_length=64)



class Branch(models.Model):
    branch=models.CharField(max_length=64)

class Year(models.Model):
    year=models.CharField(max_length=64)



class Material(models.Model):
    ids=models.AutoField(primary_key=True)
    program=models.CharField(max_length=64)
    branch=models.CharField(max_length=64)
    year=models.CharField(max_length=64)
    subject=models.CharField(max_length=64)
    filename=models.CharField(max_length=64)
    myfile=models.FileField(upload_to='')
    

class News(models.Model):
    nid=models.AutoField(primary_key=True)
    newstitle=models.CharField(max_length=64,default="none")
    newsby=models.CharField(max_length=64,default="none")
    newstext=models.TextField()
    newsdate=models.CharField(max_length=64)