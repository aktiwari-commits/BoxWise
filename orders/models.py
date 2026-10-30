from django.db import models

class Order(models.Model):

    order_number = models.CharField(
        max_length=30,
        unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number
    

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )

    product = models.ForeignKey(
        'products.Products',
        on_delete=models.PROTECT,
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

