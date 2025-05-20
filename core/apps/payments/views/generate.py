from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from core.apps.havasbook.models.order import OrderModel
from payme import Payme
from config.env import env



PAYME_ID = env("PAYME_ID")


class PayLinkViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def generate(self, request):
        order_id = request.data.get("order_id")
        if not order_id:
            return Response({"error": "order_id is required"}, status=400)

        order = get_object_or_404(OrderModel, id=order_id)
        
        payme = Payme(payme_id=PAYME_ID)
        amount = int(order.total_price * 100)
        pay_link = payme.initializer.generate_pay_link(
            id=order.id,
            amount=amount,
            return_url="http://127.0.0.1:8081/"
        )
        print(pay_link)

        return Response({"pay_link": pay_link})
