from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
