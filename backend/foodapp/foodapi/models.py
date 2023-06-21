from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal = models.CharField(max_length=100)
    total = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return str(self.pk)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.pk)