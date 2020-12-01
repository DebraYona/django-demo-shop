from rest_framework import routers

from shop.views import OrderViewSet, OrderDetailViewSet

router_shop = routers.DefaultRouter()

router_shop.register(r'order', OrderViewSet, basename='order')
router_shop.register(r'order-detail', OrderDetailViewSet, basename='order-detail')
