from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Colour, Brand, CarModel, Order
from .serializers import ColourSerializer, BrandSerializer, CarModelSerializer, OrderSerializer


class ColourViewSet(viewsets.ModelViewSet):
    queryset = Colour.objects.all()
    serializer_class = ColourSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ('car_model',)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('quantity',)
