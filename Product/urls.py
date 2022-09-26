from .views import *
from rest_framework import routers
from django.urls import include, re_path

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'addproduct', addProductViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]