from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config.env import env
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = env("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

__all__ = ["bot", "dp"]
