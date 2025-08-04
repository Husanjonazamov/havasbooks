from click_up.views import ClickWebhook


import logging
logger = logging.getLogger(__name__)

class ClickWebhookAPIView(ClickWebhook):
    def successfully_payment(self, params):
        logger.info(f"✅ Payment successful. Params: {params}")

    def cancelled_payment(self, params):
        logger.warning(f"❌ Payment cancelled. Params: {params}")

    def post(self, request, *args, **kwargs):
        logger.info(f"📥 Received data: {request.POST.dict()}")
        return super().post(request, *args, **kwargs)
