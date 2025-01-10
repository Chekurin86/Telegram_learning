from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from token_1 import TOKEN
from translator import translate
from aiogram import F


BOT_TOKEN = TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer("Привет!\nМеня зовут Бот-переводчик!\nНапиши мне что-нибудь на английском "
                         "или русском языках, и я переведу тебе этот текст.")

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь, и в ответ '
        "я пришлю тебе твое сообщение,"
        "но уже переведенное на другой язык."
    )

@dp.message(F.text)
async def send_translate(message: Message):
    await message.answer("Подожди немного, и я переведу тебе этот текст")
    await message.answer(text=translate(message.text))

@dp.message()
async def send_echo(message: Message):
    await message.answer("Извините, я могу перевести только текст...")

if __name__ == '__main__':
    dp.run_polling(bot)