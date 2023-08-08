import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


TOKEN = "6593696633:AAGj-0iOtkn-lLK02-7_0QOPHFn5t1Z062Q"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

user_id = message.from_user.id
if user_id == 5008466926:
    user = "esfandyar99"
if user_id == 5738722480:
    user = "A1beba"
if user_id == 1433908907:
    user = "Jony_Noryaki"
if user_id == 5225823042:
    user = "tarel_04ka"
if user_id == 958539467:
    user = "vlruhttp"
if user_id == 5710768790:
    user = "dapofek"
if user_id == 1891071566:
    user = "sheqwe"
if user_id == 1912174022:
    user = "zennelac"
if user_id == 1861115532:
    user = "excuse_please"
if user_id == 927379439:
    user = "noctcd"
if user_id == 5114574923:
    user = "mr_bredushek"


esfandyar99_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
                    'есть 4 звезда': '?', 'есть 2 звезда': '?'}
A1beba_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
               'есть 4 звезда': '?', 'есть 2 звезда': '?'}
Jony_Noryaki_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
                     'есть 4 звезда': '?', 'есть 2 звезда': '?'}
tarel_04ka_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
                   'есть 4 звезда': '?', 'есть 2 звезда': '?'}
vlruhttp_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
                 'есть 4 звезда': '?', 'есть 2 звезда': '?'}
dapofek_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
                'есть 4 звезда': '?', 'есть 2 звезда': '?'}
sheqwe_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
               'есть 4 звезда': '?', 'есть 2 звезда': '?'}
zennelac_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
                 'есть 4 звезда': '?', 'есть 2 звезда': '?'}
excuse_please_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
                      'есть 4 звезда': '?', 'есть 2 звезда': '?'}
noctcd_data = {'астральные камни': '?', 'Сумма хар-ик': '?',
               'есть 4 звезда': '?', 'есть 2 звезда': '?'}
mr_bredushek = {'астральные камни': '?', 'Сумма хар-ик': '?',
                'есть 4 звезда': '?', 'есть 2 звезда': '?'}


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global user
    btn_menu_1 = KeyboardButton('Созвездия')
    # btn_menu_2 = KeyboardButton('Тут что то будет')
    menu = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    menu.add(btn_menu_1)
    # menu.add(btn_menu_2)
    await message.answer("Приветствую тебя в боте Морфиона.", reply_markup=menu)
    await message.answer(f"Вы {user}")


@dp.message_handler(text='Созвездия')
async def handle_atack(message: types.Message):
    btn_stars_1 = KeyboardButton('4 звезда')
    btn_stars_2 = KeyboardButton('2 звезда')
    stars = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    stars.add(btn_stars_1)
    stars.add(btn_stars_2)
    await message.answer("Возможно вам откроются тайны созвездий, какую тайну вы хотите раскрыть? Вдруг звезда раскроет перед вами новый путь и ваше созвездие получит новое сияние", reply_markup=stars)

# @dp.message_handler(text='4 звезда')
# async def handle_atack(message: types.Message):
   # if 'Сумма хар-ик' in my_dict and my_dict['ключ2'] == 56:
   # await message.answer("")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
