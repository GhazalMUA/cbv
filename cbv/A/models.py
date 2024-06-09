from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    owner=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Kelas(models.Model):
    name=models.CharField(max_length=100)
    coach=models.CharField(max_length=100)
    price=models.SmallIntegerField()
    
    def __str__(self):
        return self.name