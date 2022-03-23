from django.db import models

# Create your models here.
class Species(models.Model):
    name=models.CharField(max_length=60)
    classification=models.CharField(max_length=60)
    language=models.CharField(max_length=60)
    
    
    
class Person(models.Model):
    name=models.CharField(max_length=60)
    birth_year=models.CharField(max_length=10)
    eye_color=models.CharField(max_length=10)
    species=models.ForeignKey(Species, on_delete=models.DO_NOTHING)
    