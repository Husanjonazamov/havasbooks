import telebot
from telebot import types
from django.core.management.base import BaseCommand
from .loader import bot
from config.env import env
from core.apps.bot.management.commands.handler import *


ADMIN_ID = env.int('ADMIN_ID')

class Command(BaseCommand):
    help="Botni ishga tushirish"
    
    def handle(self, *args, **options):
        bot.send_message(ADMIN_ID, text="bot ishga tushdi")
        
        self.stdout.write("bot ishga tushirildi")
        bot.polling()










