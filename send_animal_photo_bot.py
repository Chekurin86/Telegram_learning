from token_1 import TOKEN
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F


API_URL = 'https://api.telegram.org/bot'

CATS_API_URL = "https://api.thecatapi.com/v1/images/search"
DOGS_API_URL = "https://random.dog/woof.json"
FOXES_API_URL = "https://randomfox.ca/floof/"
CAPYBARA_API_URL = "https://api.capy.lol/v1/capybara?json=true"

BOT_TOKEN = TOKEN
ERROR_TEXT = 'Здесь должна была быть картинка с животным... :('
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

url_list = [(CATS_API_URL, 0, 'url'), (DOGS_API_URL, 'url'),
            (FOXES_API_URL, 'link'), (CAPYBARA_API_URL, 'data', 'url')]

offset = -2
counter = 0
animal_response: requests.Response
cat_link: str


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer("Привет!\nЯ Бот, и я могу показать какую-нибудь случайную фотографию животного, которое ты выберешь.\n"
    "Напиши мне какое бы ты хотел увидеть животное из данного списка, и я тебе его найду!")


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        "Напиши какое бы ты хотел увидеть животное: кошку, собак, лису или капибару.\n"    
        "И я пришлю тебе случайную фотографию выбранного вами животного."
    )

@dp.message(F.text)
async def send_animal_photo(message: Message):
    if ("кот" in message.text.lower()) or ("кош" in message.text.lower()):
        animal_response = requests.get(CATS_API_URL)
        await bot.send_photo(chat_id=message.chat.id, photo=animal_response.json()[0]['url'])
    if ("соб" in message.text.lower()) or ("щен" in message.text.lower()):
        animal_response = requests.get(DOGS_API_URL)
        await bot.send_photo(chat_id=message.chat.id, photo=animal_response.json()['url'])
    if ("лис" in message.text.lower()):
        animal_response = requests.get(FOXES_API_URL)
        await bot.send_photo(chat_id=message.chat.id, photo=animal_response.json()['link'])
    if ("кап" in message.text.lower()):
        animal_response = requests.get(CAPYBARA_API_URL)
        await bot.send_photo(chat_id=message.chat.id, photo=animal_response.json()['data']['url'])


@dp.message()
async def send_echo(message: Message):
    await message.answer("Извините, я смогу отправить вам изображение только если вы напишите мне название животного из списка...")

if __name__ == '__main__':
    dp.run_polling(bot)

