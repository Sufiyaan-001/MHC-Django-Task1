from django.db import models

# Create your models here.
class cloths(models.Model):
    Name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Shipping_agent = models.CharField(max_length=255)
    Size = models.CharField(max_length=10)
    Price = models.IntegerField()
    
    def __str__(self):
        return f"{self.Name} {self.Type}"
    