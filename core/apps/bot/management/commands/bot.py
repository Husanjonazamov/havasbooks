import telebot
from config.env import env


BOT_TOKEN = env.str('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)






