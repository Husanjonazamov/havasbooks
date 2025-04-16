import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from core.apps.havasbook.models import BookModel, LocationModel

bot = telebot.TeleBot("7178118588:AAHtJ8mKY-ChU0yyxiyWhcVogURQwki61_Y")

def send_order_to_telegram(order, location_name, latitude, longitude):
    chat_id = "5765144405"
    google_maps_url = f"https://yandex.com/maps/?pt={longitude},{latitude}&z=14&l=map"

    # 🧭 Tugma (manzil uchun)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📍 Manzilni ko‘rish", url=google_maps_url))

    order_items = order.order_item.all()

    # 🧾 Buyurtma haqida asosiy caption
    caption = (
        f"📦 <b>Yangi Buyurtma</b> #{order.id}\n\n"
        f"👤 <b>Mijoz raqami:</b> {order.phone}\n"
        f"📍 <b>Joylashuv:</b> {location_name}\n"
        f"💰 <b>Jami summa:</b> {int(order.total_amount):,} so'm\n"
        f"🗒️ <b>Izoh:</b> {order.comment or 'Yo‘q'}\n\n"
        f"📚 <b>Buyurtmadagi kitoblar:</b>\n"
    )

    image_paths = []

    # 🔢 Kitoblar tartib raqami bilan chiqariladi
    for idx, item in enumerate(order_items, 1):
        book = item.book
        caption += (
            f"\n{idx}. <b>{book.name}</b>\n"
            f"   💵 Narxi: {int(item.price):,} so'm\n"
            f"   📦 Miqdori: {item.quantity} dona\n"
        )
        if book.image:
            image_paths.append(book.image.path)

    # 🖼️ Rasmlar bo‘yicha ishlov
    if len(image_paths) > 1:
        media_group = []
        for idx, path in enumerate(image_paths):
            with open(path, 'rb') as img:
                img_data = img.read()
                if idx == 0:
                    media_group.append(InputMediaPhoto(img_data, caption=caption, parse_mode="HTML"))
                else:
                    media_group.append(InputMediaPhoto(img_data))
        bot.send_media_group(chat_id=chat_id, media=media_group)

        # 📍 Manzil tugmasi alohida yuboriladi
        bot.send_message(
            chat_id=chat_id,
            text="📍 <b>Manzilni ko‘rish uchun tugmani bosing:</b>",
            parse_mode="HTML",
            reply_markup=markup
        )

    elif len(image_paths) == 1:
        with open(image_paths[0], 'rb') as photo:
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
