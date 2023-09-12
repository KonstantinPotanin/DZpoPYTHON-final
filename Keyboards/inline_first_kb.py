from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first_course = InlineKeyboardMarkup(row_width=1)
first_course.add(InlineKeyboardButton(text='Лагман', url='https://www.russianfood.com/recipes/recipe.php?rid=134958'),
                 InlineKeyboardButton(text='Солянка', url='https://www.russianfood.com/recipes/recipe.php?rid=125910'),
                 InlineKeyboardButton(text='Сырный суп', url='https://www.russianfood.com/recipes/recipe.php?rid=135251'))
