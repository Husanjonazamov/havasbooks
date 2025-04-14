from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django_core.paginations import CustomPagination

from ..models import BookimageModel, BookModel
from ..serializers.book import (
    CreateBookimageSerializer,
    CreateBookSerializer,
    ListBookimageSerializer,
    ListBookSerializer,
    RetrieveBookimageSerializer,
    RetrieveBookSerializer,
)

from django.db.models import Q

class BooksSearchView(ModelViewSet):
    serializer_class = ListBookSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = BookModel.objects.all()
        q = self.request.query_params.get('search', None)

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(description__icontains=q)  # kerakli fieldlarni qo‘shasiz
            )
        return queryset



@extend_schema(tags=["book"])
class BookView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = ListBookSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBookSerializer,
        "retrieve": RetrieveBookSerializer,
        "create": CreateBookSerializer,
    }




@extend_schema(tags=["bookImage"])
class BookimageView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BookimageModel.objects.all()
    serializer_class = ListBookimageSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBookimageSerializer,
        "retrieve": RetrieveBookimageSerializer,
        "create": CreateBookimageSerializer,
    }
