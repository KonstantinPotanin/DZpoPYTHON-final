from aiogram.types import Message
from loader import dp


@dp.message_handler()
async def start_bot(message: Message):
    await message.reply(f'{message.from_user.first_name}, я не понимаю этой команды, попробуй сначала: /start')
