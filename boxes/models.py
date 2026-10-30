from django.db import models
from django.core.validators import MinValueValidator


class Box(models.Model):

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

    height = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    max_weight = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)]
    )

    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name