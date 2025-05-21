import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from core.apps.havasbook.models import BookModel
from core.apps.havasbook.serializers.order.generate_link import send_payment_options
from config.env import env

BOT_TOKEN = env("BOT_TOKEN")
CHANNEL_ID = env.int("CHANNEL_ID")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')  


def send_preorder_to_telegram(preorder, request):
    chat_id = CHANNEL_ID

    caption = (
        f"📦 <b>Yangi Buyurtma</b> #{preorder.id}\n\n"
        f"👤 <b>Buyurtmachi:</b> {preorder.user_name}\n"
        f"📞 <b>Telefon:</b> {preorder.phone}\n"
        f"💰 <b>Jami summa:</b> {int(preorder.total_price):,} so'm\n"
        f"📚 <b>Buyurtmadagi kitoblar:</b>\n"
    )

    book = preorder.book
    caption += (
        f"   <b>{book.name}</b>\n"
        f"   💵 Narxi: {int(book.price):,} so'm\n"
        f"   📦 Miqdori: {preorder.count} dona\n"
    )

    if book.image and book.image.path:
        with open(book.image.path, 'rb') as img:
            bot.send_photo(chat_id=chat_id, photo=img, caption=caption, parse_mode="HTML")
    else:
        bot.send_message(chat_id=chat_id, text=caption, parse_mode="HTML")
