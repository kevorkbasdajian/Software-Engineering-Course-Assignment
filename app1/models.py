from django.db import models

# Create your models here.



class Movie(models.Model):
    ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    year = models.IntegerField()
    rating = models.FloatField()
    director = models.CharField(max_length = 100)
    description = models.CharField(max_length=500)
    


