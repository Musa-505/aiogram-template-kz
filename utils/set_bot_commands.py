from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botti qayta iske qosu"),
            types.BotCommand("help", "Ko'mek"),
        ]
    )
