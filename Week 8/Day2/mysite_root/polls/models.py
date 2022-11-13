from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.TextField()
    
class Animal(models.Model):
    legs = models.CharField(max_length=40)
    weight = models.FloatField(max_length=4)
    height = models.BigIntegerField(max_length=4)
    speed = models.IntegerField()
    family = models.ForeignKey(Family,on_delete=models.CASCADE)




