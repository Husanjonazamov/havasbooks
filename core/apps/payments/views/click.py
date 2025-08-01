from payme.views import PaymeWebHookAPIView
from core.apps.havasbook.models.order import OrderModel

import logging

from click_up.views import ClickWebhook
from click_up.models import ClickTransaction
from core.apps.havasbook.serializers.order.send_order import send_user_order, send_payment_success



class ClickWebhookAPIView(ClickWebhook):
    """
    A view to handle Click Webhook API calls.
    This view will handle all the Click Webhook API events.
    """
    def successfully_payment(self, params):
        """
        Successfully payment method process you can override it.
        """
        try:
            transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
            )
        
            order = OrderModel.objects.get(id=transaction.account_id)

            
            send_user_order(order)
            send_payment_success(order)
        except OrderModel.DoesNotExist:
            raise Exception("Order not found")


    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )

        if transaction.state == ClickTransaction.CANCELLED:
            order = OrderModel.objects.get(id=transaction.account_id)
            order.is_finishid = False
            order.save()
