from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

second_course = InlineKeyboardMarkup(row_width=1)
second_course.add(InlineKeyboardButton(text='Мясо по-французски', url='https://www.russianfood.com/recipes/recipe.php?rid=132942'),
                 InlineKeyboardButton(text='Овощное рагу', url='https://www.russianfood.com/recipes/recipe.php?rid=146523 '),
                 InlineKeyboardButton(text='Плов', url='https://www.russianfood.com/recipes/bytype/?fid=473,912'))