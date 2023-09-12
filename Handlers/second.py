from aiogram.types import Message
from loader import dp
from Keyboards import second_course


@dp.message_handler(text='Второе блюдо')
async def course_second(message: Message):
    await message.answer('Второе блюдо', reply_markup=second_course)