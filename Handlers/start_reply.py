from aiogram.types import Message
from loader import dp
from Keyboards import keyboard


@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    await message.answer(f'{message.from_user.first_name}, привет! Могу предложить несколько рецептов '
                         f'для приготовления блюд в мультиварке.', reply_markup=keyboard)
