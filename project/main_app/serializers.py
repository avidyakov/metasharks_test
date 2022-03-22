from django.db.models import Sum
from rest_framework import serializers

from .models import Colour, Brand, CarModel, Order


class ColourSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Colour
        fields = ('id', 'name', 'orders')

    def get_orders(self, colour) -> int:
        return colour.orders.aggregate(Sum('quantity')).get('quantity__sum')


class BrandSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ('id', 'name', 'orders')

    def get_orders(self, brand) -> int:
        return brand.models.aggregate(Sum('orders__quantity')).get('orders__quantity__sum')


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'name', 'brand')
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'created', 'quantity', 'colour', 'car_model')
        depth = 2
