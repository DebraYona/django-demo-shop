"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.routers import router_core
from shop.routers import router_shop
from shop.views.order import AddProductToCartAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('core/', include(router_core.urls), name='core'),
    path('shop/', include(router_shop.urls), name='shop'),
    path('add-product/', AddProductToCartAPIView.as_view(), name='add-product'),
    path('api-auth/', include('rest_framework.urls'))
]
