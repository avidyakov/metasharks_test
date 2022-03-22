from rest_framework import routers

from .views import ColourViewSet, BrandViewSet, CarModelViewSet, OrderViewSet

app_name = 'main_app'

router = routers.SimpleRouter()
router.register('colors', ColourViewSet)
router.register('brands', BrandViewSet)
router.register('car_models', CarModelViewSet)
router.register('orders', OrderViewSet)

urlpatterns = router.urls
