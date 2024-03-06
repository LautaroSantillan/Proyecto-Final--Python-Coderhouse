from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name} {self.lastname}"
    
class Client(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.lastname}"
    
class Activity(models.Model):
    name = models.CharField(max_length=40)
    day = models.CharField(max_length=10)
    hour = models.IntegerField()
    def __str__(self):
        return f"{self.name}"
    
class Place(models.Model):
    street = models.CharField(max_length=40)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.street} {self.number} - {self.city} - {self.province}"