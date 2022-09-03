from pickle import TRUE
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    contact=models.PositiveBigIntegerField()
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    password1=models.CharField(max_length=40)

class Student(models.Model):
    sid=models.IntegerField(primary_key=TRUE)
    sname=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    SUBJECTS=[
        ("1","maths"),
        ("2","physics"),
        ("3","computers")
        ]
    subject=models.CharField(max_length=40,choices=SUBJECTS,default=1)
    contact=models.PositiveIntegerField()
    
    def __str__(self):
        return self.sname

class Student1(models.Model):
    sid=models.IntegerField(primary_key=TRUE)
    sname=models.CharField(max_length=40)
    fee=models.PositiveIntegerField()
    doj=models.DateField()
   
    def __str__(self):
        return self.sname


class Student2(models.Model):
    sname=models.CharField(max_length=30)
    std_image=models.ImageField(upload_to='media/images/')
    std_profile=models.FileField(upload_to='media/files/')
    
    def __str__(self):
        return self.sname

class P(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=40)
    courses=models.CharField(max_length=30)