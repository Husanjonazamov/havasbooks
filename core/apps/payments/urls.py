from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.payments.views import (
    PaymeCallBackAPIView, OrderPaymentLinkView
) 

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("payment/update/", PaymeCallBackAPIView.as_view()),
    path("payment/payme/", OrderPaymentLinkView.as_view()),
    
]
