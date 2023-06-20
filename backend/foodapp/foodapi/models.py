from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name