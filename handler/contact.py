from aiogram import types, F, Router
from loader import bot
from utils import texts, keyboard

router = Router()

@router.message(F.text.startswith(keyboard.CONTACT))
async def contact(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=texts.CONTACTS
    )
