from aiogram.types import Message
from loader import dp
from Keyboards import first_course


@dp.message_handler(text='Первое блюдо')
async def course_first(message: Message):
    await message.answer('Первое блюдо', reply_markup=first_course)
