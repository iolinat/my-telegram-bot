import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


TOKEN = "6593696633:AAGj-0iOtkn-lLK02-7_0QOPHFn5t1Z062Q"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler()
async def handle_atack(message: types.Message):
    chance = random.randint(1, 99)
    if chance <= 33:
        Hui_or_pizda = "Хуй хуй хуй"
    if chance > 33 and chance <= 66:
        Hui_or_pizda = "Хуй пизда хуй пизда"
    if chance >= 67:
        Hui_or_pizda = "Пизда пизда пизда"
    await message.answer(f"{Hui_or_pizda}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
