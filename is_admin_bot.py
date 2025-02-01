from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, BaseFilter
from token_1 import TOKEN

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = TOKEN

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Список с ID администраторов бота
admins_ids: list[int] = [6991696753]

# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admins_ids: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admins_ids = admins_ids
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins_ids

# Этот хендлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admins_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text="Вы админ")

# Этот хендлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text="Вы не админ")

if __name__ == '__main__':
    dp.run_polling(bot)





# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer(text='Это команда /start')


if __name__ == '__main__':
    dp.run_polling(bot)

# print(message.model_dump_json(indent=4, exclude_none=True))