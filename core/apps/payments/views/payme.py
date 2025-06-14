from payme.views import PaymeWebHookAPIView
from core.apps.havasbook.serializers.order.send_order import send_user_order, send_payment_success
from core.apps.havasbook.models import OrderModel
import logging
from payme.models import PaymeTransactions

class PaymeCallBackAPIView(PaymeWebHookAPIView):
    def handle_created_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction created for this params: {params} and cr_result: {result}")


    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        try:
            transaction_id = int(params.get("account", {}).get("id"))
            raise Exception(PaymeTransactions.objects.filter(transaction_id=transaction_id))
            order_id = None
            order = OrderModel.objects.get(id=order_id)
            print(f"Order: id {order_id}")
            print(f"bu parasms: {params}") 
            print(f"bu accoun: {params.get("account", {})}")  
            print(f"bu params id: {params.get("account", {}).get("id")}")  
            send_user_order(order)
            send_payment_success(order)
        except OrderModel.DoesNotExist:
            print(f"Order with ID not found.")     
        except Exception as e:
            print(e)
                   

        print(f"Transaction successfully performed for this params: {params} and performed_result: {result}")

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        print(f"Transaction cancelled for this params: {params} and cancelled_result: {result}")
        



