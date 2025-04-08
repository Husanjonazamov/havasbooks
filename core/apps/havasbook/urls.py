from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.havasbook.views import (
    BannerView,
    CategoryView,
    BookView,
    CartitemView,
    CartView
)

router = DefaultRouter()
router.register(r"banner", BannerView, basename='banner')
router.register(r"category", CategoryView, basename='category')
router.register(r"books", BookView, basename='books')
router.register(r"cart", CartView, basename='cart')
router.register(r"cart-item", CartitemView, basename='cart-item')




urlpatterns = [
    path("", include(router.urls)),
]
