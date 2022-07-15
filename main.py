from aiogram import types
from aiogram.utils import executor
from AdminBot import FSMadmin
from config import bot, dp

async def on_startup(_):
    print('Bot is online')
@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await bot.send_message(message.chat.id,
                           f'Здравствуйте теперь у вас работает бот который зашитит от других ботов!')


FSMadmin.register_handler_admin(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)