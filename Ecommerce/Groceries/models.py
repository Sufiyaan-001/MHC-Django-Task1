from django.db import models

# Create your models here.
class groces(models.Model):
    Name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Quality = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    Vendor = models.CharField(max_length=255)
    Price = models.IntegerField()
    
    def __str__(self):
        return f"{self.Name} {self.Type}"
    