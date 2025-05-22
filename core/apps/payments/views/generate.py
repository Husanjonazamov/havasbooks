from rest_framework import status, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.apps.havasbook.models.order import OrderModel
from core.apps.accounts.models.user import User

from payme import Payme
from config.env import env

PAYME_ID = env("PAYME_ID")
payme = Payme(payme_id=PAYME_ID)


class OrderPaymentLinkView(views.APIView):
    def post(self, request):
        order_id = request.data.get("order_id")
        if not order_id:
            return Response({"error": "order_id is required"}, status=400)

        order = get_object_or_404(OrderModel, id=order_id)

        if not order.user:  
            return Response({"error": "Orderga bog'liq foydalanuvchi topilmadi"}, status=400)

        amount = int(order.total_price * 100)
     
        try:
            pay_link = payme.initializer.generate_pay_link(
                id=str(order.id),  
                amount=amount,
                return_url="https://t.me/jigarPrint_bot"
            )
        except Exception as e:
            return Response({"error": f"Payme link yaratishda xatolik: {str(e)}"}, status=500)

        result = {
            "order_id": order.id,
            "user_id": order.user.user_id,
            "total_price": order.total_price,
            "pay_link": pay_link
        }

        return Response(result, status=200)
