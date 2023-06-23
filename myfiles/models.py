from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    deadline = models.DateField()
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    description = models.TextField()
    picture1 = models.ImageField(upload_to='media')
    picture2 = models.ImageField(upload_to='media',null=True,blank=True)
    picture3 = models.ImageField(upload_to='media',null=True,blank=True)
    date = models.DateTimeField(auto_now=True)

class Services(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='media')
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Team(models.Model):
    name = models.CharField(max_length=50)
    lavozim = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='media')
    link1 = models.CharField(max_length=200)
    link2 = models.CharField(max_length=200)
    link3 = models.CharField(max_length=200)
    link4 = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Malumot_saqlash(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Subject(models.Model):
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

class Subj(models.Model):
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

class Ali(models.Model):
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)








