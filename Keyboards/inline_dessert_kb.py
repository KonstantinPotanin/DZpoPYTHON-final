from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

dessert = InlineKeyboardMarkup(row_width=1)
dessert.add(InlineKeyboardButton(text='Бисквит', url='https://www.russianfood.com/recipes/recipe.php?rid=124817'),
                 InlineKeyboardButton(text='Манник', url='https://www.russianfood.com/recipes/recipe.php?rid=135281'),
                 InlineKeyboardButton(text='Яблочная шарлотка', url='https://www.russianfood.com/recipes/recipe.php?rid=133424'))