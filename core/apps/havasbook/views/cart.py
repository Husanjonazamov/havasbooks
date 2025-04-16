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
    
    
class CartitemView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CartitemModel.objects.all()
    serializer_class = ListCartitemSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartitemSerializer,
        "retrieve": RetrieveCartitemSerializer,
        "create": CreateCartitemSerializer,
    }
    
    def destroy(self, request, pk=None):
        self.permission_classes = [IsAuthenticated]
        
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        
        cart_item = get_object_or_404(CartitemModel, pk=pk, cart__user=request.user)

        cart = cart_item.cart
        cart.total_price -= cart_item.total_price  
        cart.save()  

        cart_item.delete()

        return Response({'status': True}, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        self.permission_classes = [IsAuthenticated]
    
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
            
        quantity = request.data.get("quantity")
        cart_item = get_object_or_404(CartitemModel, pk=pk, cart__user=request.user) 
        
        new_total_price = cart_item.book.price * quantity  
        old_total_price = cart_item.total_price  

        cart_item.quantity = quantity
        cart_item.total_price = new_total_price
        cart_item.save()

        cart = cart_item.cart

        cart.total_price += (new_total_price - old_total_price) 
        cart.save() 

        cart_item_serializer = ListCartitemSerializer(cart_item)
        cart_serializer = ListCartSerializer(cart)

        return Response(
            {
                "status": True,
                "message": "Quantity and total_price updated successfully",
                "data": {
                    "cart_item": cart_item_serializer.data,
                    "cart": cart_serializer.data
                }
            },
            status=status.HTTP_200_OK
        )