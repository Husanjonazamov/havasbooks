from . import start
from . import contact
from . import generate

from aiogram import Dispatcher

def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(contact.router)
