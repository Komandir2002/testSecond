from aiogram import types,Dispatcher
from config import bot


async def antybot(message:types.Message):
    if message.from_user.bot:
        print('бот зашел вгруппу!!!')


def register_handler_admin(dp:Dispatcher):
    dp.register_message_handler(antybot)