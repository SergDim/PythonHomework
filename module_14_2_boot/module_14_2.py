
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import bot_key

bot = Bot(token=bot_key.TELEGRAMM_BOT_API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_massage(message):
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)