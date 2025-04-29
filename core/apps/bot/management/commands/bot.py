import telebot
from telebot import types
from config.env import env
from django.core.management.base import BaseCommand

import logging

BOT_TOKEN = env.str('BOT_TOKEN')
ADMIN_ID = env.int('ADMIN_ID')

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    help="Botni ishga tushirish"
    
    def handle(self, *args, **options):
        bot.send_message(ADMIN_ID, text="bot ishga tushdi")
        @bot.message_handler(commands=['start'])
        def start_handler(message: types.Message):
            bot.send_message(chat_id=message.from_user.id, text="salom")
            
        self.stdout.write("bot ishga tushirildi")
        bot.polling()










