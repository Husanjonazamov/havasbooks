import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from core.apps.havasbook.models import BookModel
from core.apps.havasbook.serializers.order.generate_link import send_payment_options

bot = telebot.TeleBot("7178118588:AAHtJ8mKY-ChU0yyxiyWhcVogURQwki61_Y")


def send_order_to_telegram(order, location_name, latitude, longitude):
    send_payment_options(order, bot)

    chat_id ="-1002264446732"
    yandex_url = f"https://yandex.com/maps/?pt={longitude},{latitude}&z=14&l=map"

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📍 Manzilni ko‘rish", url=yandex_url))

    caption = (
        f"📦 <b>Yangi Buyurtma</b> #{order.id}\n\n"
        f"👤 <b>Buyurtmachi:</b> {order.reciever_name}\n"
        f"📞 <b>Telefon:</b> {order.reciever_phone}\n"
        f"📍 <b>Joylashuv:</b> {location_name}\n"
        f"💰 <b>Jami summa:</b> {int(order.total_amount):,} so'm\n"
        f"🗒️ <b>Izoh:</b> {order.comment or 'Yo‘q'}\n"
        f"💳 <b>To'lov turi:</b> {order.payment_method.capitalize()}\n\n"
        f"📚 <b>Buyurtmadagi kitoblar:</b>\n"
    )

    image_paths = []
    order_items = order.order_item.all()

    for idx, item in enumerate(order_items, 1):
        book = item.book
        caption += (
            f"\n{idx}. <b>{book.name}</b>\n"
            f"   💵 Narxi: {int(item.price):,} so'm\n"
            f"   📦 Miqdori: {item.quantity} dona\n"
        )

        if book.image and book.image.path:
            image_paths.append(book.image.path)

    if image_paths:
        media_group = []
        for i, path in enumerate(image_paths):
            with open(path, 'rb') as img:
                media = InputMediaPhoto(img.read())
                if i == 0:
                    media.caption = caption
                    media.parse_mode = "HTML"
                media_group.append(media)

        bot.send_media_group(chat_id=chat_id, media=media_group)
        bot.send_message(chat_id=chat_id, text="📍 <b>Manzilni ko‘rish uchun tugmani bosing:</b>", parse_mode="HTML", reply_markup=markup)
    
    else:
        bot.send_message(chat_id=chat_id, text=caption, parse_mode="HTML", reply_markup=markup)
