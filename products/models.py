from django.db import models
from django.core.validators import MinValueValidator


class Products(models.Model):

    name = models.CharField(max_length=100)

    length = models.DecimalField(
         max_digits=8, 
         decimal_places=2, 
         validators=[MinValueValidator(0.01)]
        
                  
    )

    width = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

# Create your models here.
    height = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


