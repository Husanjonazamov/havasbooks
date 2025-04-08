from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CartModel
from ..serializers.cart import CreateCartSerializer, ListCartSerializer, RetrieveCartSerializer


@extend_schema(tags=["cart"])
class CartView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = ListCartSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartSerializer,
        "retrieve": RetrieveCartSerializer,
        "create": CreateCartSerializer,
    }
