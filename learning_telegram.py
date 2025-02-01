from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, BaseFilter
from token_1 import TOKEN

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = TOKEN

# Этот фильтр будет проверять наличие неотрицательных чисел
#

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



if __name__ == '__main__':
    dp.run_polling(bot)






# print(message.model_dump_json(indent=4, exclude_none=True))