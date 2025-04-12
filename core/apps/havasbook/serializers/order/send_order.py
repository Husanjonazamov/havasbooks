import telebot
from telebot import types
from core.apps.havasbook.models import BookModel, LocationModel


bot = telebot.TeleBot("7178118588:AAHtJ8mKY-ChU0yyxiyWhcVogURQwki61_Y")


def send_order_to_telegram(order, location_name, latitude, longitude):
    chat_id = "5765144405"

    google_maps_url = f"https://yandex.com/maps/?pt={longitude},{latitude}&z=14&l=map"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📍 Manzilni ko‘rish", url=google_maps_url))

    # Xabarning asosiy qismini tayyorlash
    caption = (
        f"📘 Buyurtma: {order.id}\n"
        f"📞 Tel: {order.phone}\n"
        f"📍 Joylashuv: {location_name}\n"
        f"💰 Umumiy narx: {order.total_amount} so'm\n"
        f"💬 Izoh: {order.comment or 'Yo\'q'}\n"
        f"📦 Buyurtma elementlari:\n"
    )
    
    # Har bir order_item uchun ma'lumotlarni qo'shish
    for item in order.order_item.all():
        book = item.book
        caption += (
            f"\n📘 Kitob: <b>{book.name}</b>\n"
            f"💵 Narxi: {item.price} so'm\n"
            f"📦 Miqdori: {item.quantity} ta\n"
        )

    # Rasmni tekshirish va yuborish
    if item.book.image:
        image_path = item.book.image.path
        with open(image_path, 'rb') as photo:
            bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=markup
            )
    else:
        bot.send_message(
            chat_id=chat_id,
            text=caption,
            parse_mode="HTML",
            reply_markup=markup
        )
