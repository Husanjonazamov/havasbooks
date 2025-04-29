from telebot.types import (
    ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
)



CONTACT = "📞 Bog'lanish"


def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    shop = KeyboardButton(
        "🛍 Magazin",
        web_app=WebAppInfo(url="https://book-web-app-lilac.vercel.app/")
    )
    keyboard.add(shop)
    
    ordering = KeyboardButton(
        "📦 Buyurtmalarim",
        web_app=WebAppInfo(url="https://book-web-app-lilac.vercel.app/")
    )
    sale = KeyboardButton(
        "🔥 Aksiyalar",
        web_app=WebAppInfo(url="https://book-web-app-lilac.vercel.app/")
    )
    keyboard.add(sale, ordering)
    
    
    contact = KeyboardButton(
        CONTACT
    )
    
    keyboard.add(contact)
    
    return keyboard

