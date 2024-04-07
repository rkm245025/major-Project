from django.db import models

# Create your models here.
class Registration(models.Model):
    username=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=500)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    fname=models.CharField(max_length=500)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    address=models.TextField()
    email=models.EmailField(max_length=64)
    regdate=models.CharField(max_length=30)
    aadhar=models.CharField(max_length=12,default=0)
    def __str__(self) -> str:
        return f"{self.name} Branch-{self.branch} Year-{self.year}"




class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.userid} {self.usertype}"



class Enquiry(models.Model):
    name=models.CharField(max_length=64)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    email=models.EmailField(max_length=64)
    enquirytext=models.TextField()
    enquirydate=models.DateField()









