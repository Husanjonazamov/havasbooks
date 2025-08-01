# from config.env import env
# import requests
# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from core.apps.havasbook.models.order import OrderModel


# BOT_TOKEN=env.str("BOT_TOKEN")
# ADMIN=env.int("ADMIN_ID")

# def send_telegram_message(order):
#     bot_token = BOT_TOKEN
#     chat_id = order.user.user_id  
    
#     url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
#     data = {
#         "chat_id": chat_id,
#         "text": f"Sizning buyurtmangiz yo'lga chiqdi. Buyurtma raqami #{order.id}"
#     }
#     try:
#         requests.post(url, data=data)
#     except Exception as e:
#         print("Telegramga xabar yuborishda xatolik:", e)
        
        
        
        
# def mark_ready_view(request, pk):
#     order = get_object_or_404(OrderModel, pk=pk)
#     if order.status != 'ready':
#         order.status = 'ready'
#         order.save()
#         send_telegram_message(order) 
#         messages.success(request, f"Buyurtma #{order.id} tayyor deb belgilandi.")
#     else:
#         messages.info(request, f"Buyurtma #{order.id} allaqachon tayyor.")
#     return redirect(request.META.get('HTTP_REFERER', '/'))