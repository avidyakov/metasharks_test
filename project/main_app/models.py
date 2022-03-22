from django.db import models


class Colour(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=127)

    brand = models.ForeignKey('main_app.Brand', on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.name


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField()

    colour = models.ForeignKey('main_app.Colour', on_delete=models.CASCADE, related_name='orders')
    car_model = models.ForeignKey('main_app.CarModel', on_delete=models.CASCADE, related_name='orders')
