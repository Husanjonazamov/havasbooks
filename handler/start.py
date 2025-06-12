from aiogram import Router, F
from aiogram.types import Message, MenuButtonWebApp, WebAppInfo
from loader import bot  # bot loader.py dan olinadi
from config.env import env
from utils import get_inline_keyboard, texts  # sizning utilslaringiz

router = Router()

# /start komandasi uchun handler
@router.message(F.text == "/start")
async def start_handler(message: Message):
    web_app_info = WebAppInfo(url=env("WEB_APP_URL"))
    menu_button = MenuButtonWebApp(
        type="web_app",
        text="📦 Magazin",
        web_app=web_app_info
    )

    # Chat menyusiga WebApp tugmasini qo‘shish
    await bot.set_chat_menu_button(chat_id=message.chat.id, menu_button=menu_button)

    # Start matnini yuborish
    await message.answer(
        text=texts.START.format(message.from_user.first_name),
        reply_markup=get_inline_keyboard()
    )
