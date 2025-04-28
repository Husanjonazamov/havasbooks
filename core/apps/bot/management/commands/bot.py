import telebot
from telebot import types
from config.env import env


BOT_TOKEN = env.str('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)




@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    bot.send_message(chat_id=message.from_user.id, text="salom")
    
    

bot.polling()










