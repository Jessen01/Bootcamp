from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField( max_length=500)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField( max_length=500)
    
     
    def __str__(self):
        return self.name
class Director(models.Model):
    first_name=models.CharField( max_length=50)  
    last_name=models.CharField( max_length=50)  
    
    def __str__(self):
        return self.first_name

class Film(models.Model):
    title=models.CharField(max_length=500)
    release_date=models.DateField( auto_now=False, auto_now_add=False)
    created_in_country=models.ForeignKey(Country, on_delete=models.CASCADE)
    available_in_countries =models.ManyToManyField(Country, related_name='categories', blank=True)
    director =models.ManyToManyField(Director, related_name='categories', blank=True)
     
    def __str__(self):
        return self.title