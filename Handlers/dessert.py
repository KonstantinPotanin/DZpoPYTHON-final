from aiogram.types import Message
from loader import dp
from Keyboards import dessert


@dp.message_handler(text='Десерт')
async def course_first(message: Message):
    await message.answer('Десерт', reply_markup=dessert)