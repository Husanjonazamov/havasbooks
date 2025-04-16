import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from core.apps.havasbook.models import BookModel, LocationModel

bot = telebot.TeleBot("7178118588:AAHtJ8mKY-ChU0yyxiyWhcVogURQwki61_Y")

def send_order_to_telegram(order, location_name, latitude, longitude):
    chat_id = "5765144405"
    google_maps_url = f"https://yandex.com/maps/?pt={longitude},{latitude}&z=14&l=map"

    # Tugma (manzil uchun)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📍 Manzilni ko‘rish", url=google_maps_url))

    order_items = order.order_item.all()

    # Caption tayyorlash
    caption = (
        f"📘 Buyurtma: {order.id}\n"
        f"📞 Tel: {order.phone}\n"
        f"📍 Joylashuv: {location_name}\n"
        f"💰 Umumiy narx: {order.total_amount} so'm\n"
        f"💬 Izoh: {order.comment or 'Yo\'q'}\n"
        f"📦 Buyurtma elementlari:\n"
    )

    image_paths = []

    for item in order_items:
        book = item.book
        caption += (
            f"\n📘 Kitob: <b>{book.name}</b>\n"
            f"💵 Narxi: {item.price} so'm\n"
            f"📦 Miqdori: {item.quantity} ta\n"
        )
        if book.image:
            image_paths.append(book.image.path)

    # Holat: 1 dan ko'p rasm bo'lsa - media_group
    if len(image_paths) > 1:
        media_group = []
        for idx, path in enumerate(image_paths):
            with open(path, 'rb') as img:
                image_data = img.read()
                if idx == 0:
                    media_group.append(InputMediaPhoto(image_data, caption=caption, parse_mode="HTML"))
                else:
                    media_group.append(InputMediaPhoto(image_data))

        # Rasm guruhini yuborish
        bot.send_media_group(chat_id=chat_id, media=media_group)

        # Tugma alohida yuboriladi
        bot.send_message(
            chat_id=chat_id,
            text="📍 <b>Manzilni ko‘rish:</b>",
            parse_mode="HTML",
            reply_markup=markup
        )

    # Holat: 1 ta rasm bo‘lsa
    elif len(image_paths) == 1:
        with open(image_paths[0], 'rb') as photo:
            bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=markup
            )

    # Holat: rasm yo‘q bo‘lsa
    else:
        bot.send_message(
            chat_id=chat_id,
            text=caption,
            parse_mode="HTML",
            reply_markup=markup
        )
