from django.db import models


class Category(models.Model):
    
    name = models.CharField(
        max_length=255, 
        unique=True
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['id']


class Product(models.Model):
    
    name = models.CharField(
        max_length=255,
        unique=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        default = 0,
        decimal_places = 2,
        max_digits = 10)
    status = models.CharField(
        max_length = 255,
        choices = [
            ('is_stock','In stock'),
            ('out_of_stock','Out of stock')
        ]
    )
    remains = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['id']