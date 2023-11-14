import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F


API_TOKEN = 'your api token'
CHAT_ID = -1234567890 # your chat id
TARGET_USERNAME = 'username' # telegram username without @


logging.basicConfig(level=logging.INFO)


dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.bot.send_message(message.from_user.id, 'hi bro')


@dp.message(F.text)
async def save_as(message: Message):
    if message.chat.id == CHAT_ID:
        if message.from_user.username == TARGET_USERNAME:
            with open('messages.txt', 'a', encoding='utf-8') as file:
                file.write(f"{message.from_user.username}: {message.text}\n")


async def main() -> None:
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())