import asyncio
import logging
from aiogram import Bot
from config.env import env
from loader import dp, bot
from handler import register_all_handlers 

ADMIN_ID = env.int("ADMIN_ID")

async def on_startup(bot: Bot):
    try:
        await bot.send_message(ADMIN_ID, "🤖 Bot ishga tushdi ✅")
    except Exception as e:
        logging.error(f"Botni ishga tushirishda xatolik: {e}")

async def main():
    register_all_handlers(dp)      
    await on_startup(bot)          
    await dp.start_polling(bot)   

if __name__ == "__main__":
    asyncio.run(main())
