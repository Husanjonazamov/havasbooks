from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import PreorderModel
from ..serializers.preorder import CreatePreorderSerializer, ListPreorderSerializer, RetrievePreorderSerializer
from django_core.paginations import CustomPagination


@extend_schema(tags=["preorder"])
class PreorderView(BaseViewSetMixin, ModelViewSet):
    queryset = PreorderModel.objects.all()
    serializer_class = ListPreorderSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPreorderSerializer,
        "retrieve": RetrievePreorderSerializer,
        "create": CreatePreorderSerializer,
    }
