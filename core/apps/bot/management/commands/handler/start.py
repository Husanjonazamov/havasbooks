from telebot import types
from ..loader import bot
from ..utils import get_keyboard
from ..utils import texts




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text=texts.START.format(message.from_user.first_name), reply_markup=get_keyboard())