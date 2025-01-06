from django.db import models

# Create your models here.
class elecs(models.Model):
    Name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Rating = models.FloatField()
    Price = models.IntegerField()
    
    def __str__(self):
        return f"{self.Name} {self.Type}"
    