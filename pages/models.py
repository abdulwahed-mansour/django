from django.db import models
import datetime
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(default=1)
    Fuel = models.CharField(max_length=30, choices=[('Unknown', 'Unknown'), ('Gasoline', 'Gasoline'), ('Hybrid', 'Hybrid'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
  

    def __str__(self):
        return self.name
    
    # Metadata
    class Meta:
        ordering = ['-created']
