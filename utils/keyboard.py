from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from config.env import env

CONTACT = "📞 Bog'lanish"
WEB_APP_URL = env("WEB_APP_URL")


def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛍 Magazin",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ],
        [
            InlineKeyboardButton(
                text="🔥 Aksiyalar",
                web_app=WebAppInfo(url=WEB_APP_URL)
            ),
            InlineKeyboardButton(
                text="📦 Buyurtmalarim",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ],
        [
            InlineKeyboardButton(
                text=CONTACT,
                callback_data="contact"
            )
        ]
    ])
    return keyboard
