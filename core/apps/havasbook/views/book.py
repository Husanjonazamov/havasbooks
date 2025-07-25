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
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.havasbook.filters.book import BookFilter


from django.shortcuts import get_object_or_404, redirect

def toggle_is_discount(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    book.is_discount = not book.is_discount
    book.save()
    
    return redirect(request.META.get('HTTP_REFERER', '/admin/'))




class BooksSearchView(ModelViewSet):
    serializer_class = ListBookSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = BookModel.objects.all()
        q = self.request.query_params.get('search', None)

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(description__icontains=q) 
            )
        return queryset




@extend_schema(tags=["book"])
class BookView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = ListBookSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = BookFilter
    ordering_fields = ['price', 'sold_count', 'view_count', 'created_at', 'popular'] 
    ordering = ['-sold_count'] 


    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBookSerializer,
        "retrieve": RetrieveBookSerializer,
        "create": CreateBookSerializer,
    }

    def get_permissions(self):
        if self.action == 'retrieve':
            from core.apps.user.permissions.user import UserPermission
            return [UserPermission()]
        return [AllowAny()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    

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


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
