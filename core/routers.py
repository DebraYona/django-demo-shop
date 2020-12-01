from rest_framework import routers

from core.views import CategoryViewSet, ProductViewSet, CategoryAndProductViewSet

router_core = routers.DefaultRouter()

router_core.register(r'category', CategoryViewSet, basename='category')
router_core.register(r'product', ProductViewSet, basename='product')
router_core.register(r'category-detail', CategoryAndProductViewSet, basename='category-detail')