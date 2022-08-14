from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyiqtar: ",
            "/start - Botti qayta iske qosu",
            "/help - Ko'mek")
    
    await message.answer("\n".join(text))
