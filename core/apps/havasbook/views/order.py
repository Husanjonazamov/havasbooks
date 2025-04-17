from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import OrderitemModel, OrderModel
from ..serializers.order import (
    CreateOrderitemSerializer,
    CreateOrderSerializer,
    ListOrderitemSerializer,
    ListOrderSerializer,
    RetrieveOrderitemSerializer,
    RetrieveOrderSerializer,
)

from rest_framework.decorators import action


@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = ListOrderSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderSerializer,
        "retrieve": RetrieveOrderSerializer,
        "create": CreateOrderSerializer,
    }
    @action(detail=False, methods=["get"], url_path="me", permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        queryset = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=["orderITem"])
class OrderitemView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderitemModel.objects.all()
    serializer_class = ListOrderitemSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderitemSerializer,
        "retrieve": RetrieveOrderitemSerializer,
        "create": CreateOrderitemSerializer,
    }
