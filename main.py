from aiogram.utils import executor
from Handlers import dp


async def on_start(_):
    print('Бот заработал')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
