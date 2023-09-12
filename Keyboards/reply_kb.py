from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_first = KeyboardButton(text='Первое блюдо')
btn_second = KeyboardButton(text='Второе блюдо')
btn_dessert = KeyboardButton(text='Десерт')

keyboard.add(btn_first).add(btn_second).add(btn_dessert)
