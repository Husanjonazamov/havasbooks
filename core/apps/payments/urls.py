from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.payments.views import (
    PaymeCallBackAPIView, PayLinkViewSet
) 

router = DefaultRouter()
router.register(r"payme", PayLinkViewSet, basename="payme")

urlpatterns = [
    path("", include(router.urls)),
    path("payment/update/", PaymeCallBackAPIView.as_view()),
]
