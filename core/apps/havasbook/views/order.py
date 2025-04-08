from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import OrderitemModel, OrderModel
from ..serializers.order import (
    CreateOrderitemSerializer,
    CreateOrderSerializer,
    ListOrderitemSerializer,
    ListOrderSerializer,
    RetrieveOrderitemSerializer,
    RetrieveOrderSerializer,
)


@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = ListOrderSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderSerializer,
        "retrieve": RetrieveOrderSerializer,
        "create": CreateOrderSerializer,
    }


@extend_schema(tags=["orderITem"])
class OrderitemView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = OrderitemModel.objects.all()
    serializer_class = ListOrderitemSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderitemSerializer,
        "retrieve": RetrieveOrderitemSerializer,
        "create": CreateOrderitemSerializer,
    }
