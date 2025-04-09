from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound



from ..models import CartitemModel, CartModel
from ..serializers.cart import (
    CreateCartitemSerializer,
    CreateCartSerializer,
    ListCartitemSerializer,
    ListCartSerializer,
    RetrieveCartitemSerializer,
    RetrieveCartSerializer,
)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action




@extend_schema(tags=["cart"])
class CartView(BaseViewSetMixin, ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = ListCartSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartSerializer,
        "retrieve": RetrieveCartSerializer,
        "create": CreateCartSerializer,
    }
    

@extend_schema(tags=["cartItem"])
class CartitemView(BaseViewSetMixin, ModelViewSet):
    queryset = CartitemModel.objects.all()
    serializer_class = ListCartitemSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartitemSerializer,
        "retrieve": RetrieveCartitemSerializer,
        "create": CreateCartitemSerializer,
    }

    def delete(self, request, pk=None):
        self.permission_classes = [IsAuthenticated]
        
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        
        cart_item = get_object_or_404(CartitemModel, pk=pk, cart__user=request.user)
        
        cart_item.delete()

        return Response({
            'status': True
        }, status=status.HTTP_200_OK)

