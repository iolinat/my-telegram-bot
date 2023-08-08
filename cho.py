import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


TOKEN = "6325630703:AAHI2cinwNJXkvzI3QCn8OLVbAliGhxXiCU"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Сейчас пройдет тест боя. Вы будете сражаться против Грахогмота.")

    global character_name
    global character_damage
    global can_destroy_iron
    global character_max_hp
    global enemy_last_move
    global character_hp
    enemy_last_move = False
    can_destroy_iron = False
    character_damage = random.randint(40, 60)
    character_max_hp = 100
    character_hp = character_max_hp
    character_name = "Иоли"

    global enemy_damage
    global enemy_max_hp
    global enemy_hp
    enemy_max_hp = 250
    enemy_damage = random.randint(40, 60)
    enemy_hp = enemy_max_hp
    await fight_start(message)


async def fight_start(message: types.Message):
    global player_choosing_move_istrue
    player_choosing_move_istrue = True
    btn_atk = KeyboardButton('🗡️Атака🗡️')
    btn_def = KeyboardButton('🛡Защита🛡')
    btn_skill = KeyboardButton('💥Навыки💥')
    btn_itm = KeyboardButton('🧪Предметы🧪')
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(btn_atk)
    keyboard.add(btn_def)
    keyboard.add(btn_skill)
    keyboard.add(btn_itm)

    await message.answer(f"""<b>Грахогмот смотрит на тебя пустыми глазами.</b>
                         
{character_name} начинает бой!""", reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text='🗡️Атака🗡️')
async def handle_atack(message: types.Message):
    global player_choosing_move_istrue
    global player_choosing_target_istrue
    if player_choosing_move_istrue == True:
        player_choosing_target_istrue = True
        player_choosing_move_istrue = False
        btn_targ_1 = KeyboardButton('Голова')
        btn_targ_2 = KeyboardButton('Брюхо')
        btn_targ_3 = KeyboardButton('Лапы')
        btn_targ_4 = KeyboardButton('Панцирь')
        btn_targ_5 = KeyboardButton('Цепи')
        targets = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True)
        targets.add(btn_targ_1)
        targets.add(btn_targ_2)
        targets.add(btn_targ_3)
        targets.add(btn_targ_4)
        targets.add(btn_targ_5)
        await message.answer(f"{character_name} целиться!", reply_markup=targets)


async def fight(message: types.Message):
    btn_atk = KeyboardButton('🗡️Атака🗡️')
    btn_def = KeyboardButton('🛡Защита🛡')
    btn_skill = KeyboardButton('💥Навыки💥')
    btn_itm = KeyboardButton('🧪Предметы🧪')
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(btn_atk)
    keyboard.add(btn_def)
    keyboard.add(btn_skill)
    keyboard.add(btn_itm)
    await message.answer(f"""<b>Грахогмот смотрит на тебя пустыми глазами.</b>
                         
{character_name} продолжает сопротивляться!""", reply_markup=keyboard, parse_mode='HTML')


async def enemy_move(message: types.Message):
    global enemy_last_move
    global enemy_hp
    global damage
    global miss
    enemy_move_choice = random.randint(1, 1)
    if enemy_move_choice == 1:
        global player_choosing_move_istrue
        enemy_attack_choice = random.randint(1, 2)
        if enemy_attack_choice == 1:
            if character_last_move == 'attack_had':
                damage = character_damage * 4
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} наносит удар прямо по голове! Грахогмот ревёт в бещенстве и с яростью смотрит на {character_name}.")
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                miss = random.randint(1, 100)
                if miss <= 80:
                    await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью. К счастью для {character_name} монстр промахнулся и стал уязвим.")
                    enemy_last_move = 'bite'
                else:
                    await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                    enemy_last_move = 'bite'
            elif character_last_move == 'attack_belly':
                damage = character_damage
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} ранит грахогмота в брюхо.")
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                enemy_last_move = 'bite'
            elif character_last_move == 'attack_paws':
                damage = character_damage
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Грахогмот лишается лапы в следствии точной атаки {character_name}.")
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                enemy_last_move = 'bite'
            elif character_last_move == 'attack_shell_completly':
                await message.answer(f"Пробивая панцирь {character_name} наносит какие-никакие повреждения грахогмоту.")
                damage = character_damage
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                enemy_last_move = 'bite'
            elif character_last_move == 'attack_shell_uncompletly':
                await message.answer(f"Послышался металлический звон. Видимо, панцирь грахогмота явно был создан из железа или чего то подобного. Неудачная и даже глупая попытка не увенчалась успехом.")
                await message.answer(f"{character_name} наносит 0 урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                enemy_last_move = 'bite'
            elif character_last_move == 'attack_chains':
                await message.answer(f"Панцирь сваливается с Страхогмота. Его брюхо очень уязвимо...")
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                enemy_last_move = 'bite'
            elif character_last_move == 'attack_chains_uncompletly':
                damage = 0
                await message.answer(f"{character_name} бьет по цепям крепящие панцирь грахогмота к чудищу. К сожалению безуспешно.")
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}!")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                enemy_last_move = 'bite'
            elif character_last_move.endswith("_miss"):
                await message.answer(f"{character_name} промахивается!")
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот сделал резкое движение головой в его сторону, с открытой во всю пастью.")
                enemy_last_move = 'bite'
            player_choosing_move_istrue = True
            await fight(message)
        elif enemy_attack_choice == 2:
            if character_last_move == 'attack_had':
                damage = character_damage * 4
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} наносит удар прямо по голове! Грахогмот ревёт в бещенстве и с яростью смотрит на {character_name}.")
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            elif character_last_move == 'attack_belly':
                damage = character_damage
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} ранит грахогмота в брюхо.")
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            elif character_last_move == 'attack_paws':
                damage = character_damage
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Грахогмот лишается лапы в следствии точной атаки {character_name}.")
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            elif character_last_move == 'attack_shell_completly':
                await message.answer(f"Пробивая панцирь {character_name} наносит какие-никакие повреждения грахогмоту.")
                damage = character_damage
                enemy_hp = enemy_hp - damage
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            elif character_last_move == 'attack_shell_uncompletly':
                await message.answer(f"Послышался металлический звон. Видимо, панцирь грахогмота явно был создан из железа или чего то подобного. Неудачная и даже глупая попытка не увенчалась успехом.")
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}.")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            elif character_last_move == 'attack_chains':
                await message.answer(f"Панцирь сваливается с Страхогмота. Его брюхо очень уязвимо...")
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            elif character_last_move == 'attack_chains_uncompletly':
                damage = 0
                await message.answer(f"{character_name} бьет по цепям крепящие панцирь грахогмота к чудищу. К сожалению безуспешно.")
                await message.answer(f"{character_name} наносит {damage} урона. Теперь жизненные силы грахогмота {enemy_hp}/{enemy_max_hp}!")
                if enemy_hp <= 0:
                    await message.answer("Грахогмот свалился без жизни.")
                    return
                else:
                    pass
                await message.answer(f"Несмотря на действияя {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            elif character_last_move.endswith("_miss"):
                await message.answer(f"{character_name} промахивается!")
                await message.answer(f"Воспользовавшись промахом {character_name}, грахогмот пошёл на таран, сбивая того с ног.")
                enemy_last_move = 'ram'
            player_choosing_move_istrue = True
            await fight(message)
    elif enemy_move_choice == 2:
        enemy_defense_choice = random.randint(1, 2)
        if enemy_defense_choice == 1:
            player_choosing_move_istrue = True
            await fight(message)
        elif enemy_defense_choice == 2:
            player_choosing_move_istrue = True
            await fight(message)


@dp.message_handler(text='Голова')
async def handle_algebra(message: types.Message):
    global player_choosing_target_istrue
    if player_choosing_target_istrue == True:
        global character_last_move
        global enemy_hp
        global miss
        global character_hp
        player_choosing_target_istrue = False
        if enemy_last_move == False:
            pass
        elif enemy_last_move == 'bite':
            miss = random.randint(1, 100)
            if miss <= 70:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 35
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот прокусывает плоть {character_name}! {character_name} орёт от боли.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        elif enemy_last_move == 'ram':
            miss = random.randint(1, 100)
            if miss <= 40:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 25
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот сбивает с ног {character_name}. Он ломает кости и становиться уязвим.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        if enemy_hp <= 0:
            await message.answer("Грахогмот свалился без жизни.")
            return
        else:
            pass
        if character_hp <= 0:
            await message.answer("Вы умерли!")
            return
        else:
            miss = random.randint(1, 100)
            if miss <= 80:
                character_last_move = 'attack_had_miss'
                await enemy_move(message)
            else:
                character_last_move = 'attack_had'
                await enemy_move(message)


@dp.message_handler(text='Брюхо')
async def handle_algebra(message: types.Message):
    global player_choosing_target_istrue
    if player_choosing_target_istrue == True:
        global character_last_move
        global enemy_hp
        global miss
        global character_hp
        player_choosing_target_istrue = False
        if enemy_last_move == False:
            pass
        elif enemy_last_move == 'bite':
            miss = random.randint(1, 100)
            if miss <= 70:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 35
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот прокусывает плоть {character_name}! {character_name} орёт от боли.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        elif enemy_last_move == 'ram':
            miss = random.randint(1, 100)
            if miss <= 40:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 25
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот сбивает с ног {character_name}. Он ломает кости и становиться уязвим.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        if enemy_hp <= 0:
            await message.answer("Грахогмот свалился без жизни.")
            return
        else:
            pass
        if character_hp <= 0:
            await message.answer("Вы умерли!")
            return
        else:
            miss = random.randint(1, 100)
            if miss <= 20:
                character_last_move = 'attack_belly_miss'
                await enemy_move(message)
            else:
                character_last_move = 'attack_belly'
                await enemy_move(message)


@dp.message_handler(text='Лапы')
async def handle_algebra(message: types.Message):
    global player_choosing_target_istrue
    if player_choosing_target_istrue == True:
        global character_last_move
        global enemy_hp
        global miss
        global character_hp
        player_choosing_target_istrue = False
        if enemy_last_move == False:
            pass
        elif enemy_last_move == 'bite':
            miss = random.randint(1, 100)
            if miss <= 70:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 35
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот прокусывает плоть {character_name}! {character_name} орёт от боли.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        elif enemy_last_move == 'ram':
            miss = random.randint(1, 100)
            if miss <= 40:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 25
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот сбивает с ног {character_name}. Он ломает кости и становиться уязвим.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        if enemy_hp <= 0:
            await message.answer("Грахогмот свалился без жизни.")
            return
        else:
            pass
        if character_hp <= 0:
            await message.answer("Вы умерли!")
            return
        else:
            miss = random.randint(1, 100)
            if miss <= 30:
                character_last_move = 'attack_paws_miss'
                await enemy_move(message)
            else:
                character_last_move = 'attack_paws'
                await enemy_move(message)


@dp.message_handler(text='Панцирь')
async def handle_algebra(message: types.Message):
    global player_choosing_target_istrue
    if player_choosing_target_istrue == True:
        global character_last_move
        global enemy_hp
        global enemy_last_move
        global character_hp
        player_choosing_target_istrue = False
        if enemy_last_move == False:
            pass
        elif enemy_last_move == 'bite':
            miss = random.randint(1, 100)
            if miss <= 70:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 35
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот прокусывает плоть {character_name}! {character_name} орёт от боли.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        elif enemy_last_move == 'ram':
            miss = random.randint(1, 100)
            if miss <= 40:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 25
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот сбивает с ног {character_name}. Он ломает кости и становиться уязвим.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        if enemy_hp <= 0:
            await message.answer("Грахогмот свалился без жизни.")
            return
        else:
            pass
        if character_hp <= 0:
            await message.answer("Вы умерли!")
            return
        else:
            if can_destroy_iron:
                character_last_move = 'attack_shell_completly'
                await enemy_move(message)
            else:
                character_last_move = 'attack_shell_uncompletly'
                await enemy_move(message)


@dp.message_handler(text='Цепи')
async def handle_algebra(message: types.Message):
    global player_choosing_target_istrue
    if player_choosing_target_istrue == True:
        global character_last_move
        global enemy_hp
        global miss
        global character_hp
        player_choosing_target_istrue = False
        if enemy_last_move == False:
            pass
        elif enemy_last_move == 'bite':
            miss = random.randint(1, 100)
            if miss <= 70:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 35
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот прокусывает плоть {character_name}! {character_name} орёт от боли.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        elif enemy_last_move == 'ram':
            miss = random.randint(1, 100)
            if miss <= 40:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 25
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот сбивает с ног {character_name}. Он ломает кости и становиться уязвим.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        if enemy_hp <= 0:
            await message.answer("Грахогмот свалился без жизни.")
            return
        else:
            pass
        if character_hp <= 0:
            await message.answer("Вы умерли!")
            return
        else:
            miss = random.randint(1, 100)
            if miss <= 40:
                character_last_move = 'attack_chains_miss'
                await enemy_move(message)
            else:
                if can_destroy_iron:
                    character_last_move = 'attack_chains'
                    await enemy_move(message)
                else:
                    character_last_move = 'attack_chains_uncompletly'
                    await enemy_move(message)


@dp.message_handler(text='🛡Защита🛡')
async def handle_geometry(message: types.Message):
    global player_choosing_move_istrue
    global player_choosing_def_istrue
    if player_choosing_move_istrue == True:
        player_choosing_def_istrue = True
        player_choosing_move_istrue = False
        btn_def_1 = KeyboardButton('Блокирование')
        btn_def_2 = KeyboardButton('Уклонение')
        targets = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True)
        targets.add(btn_def_1)
        targets.add(btn_def_2)
        await message.answer(f"{character_name} не спешит идти в атаку.", reply_markup=targets)


@dp.message_handler(text='Блокирование')
async def handle_algebra(message: types.Message):
    global player_choosing_def_istrue
    if player_choosing_def_istrue == True:
        global character_last_move
        global enemy_hp
        global miss
        global character_hp
        player_choosing_def_istrue = False
        if enemy_last_move == False:
            ###ААААААААААААА ИЗМЕНИ
            ###ААААААААААААА ИЗМЕНИ
            ###ААААААААААААА ИЗМЕНИ
            А
        elif enemy_last_move == 'bite':
            miss = random.randint(1, 100)
            if miss <= 70:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 35
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот прокусывает плоть {character_name}! {character_name} орёт от боли.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass
        elif enemy_last_move == 'ram':
            miss = random.randint(1, 100)
            if miss <= 40:
                await message.answer(f"К счастью для {character_name} монстр промахнулся и стал уязвим для атаки.")
            else:
                damage = 25
                character_hp = character_hp - damage
                await message.answer(f"Грахогмот сбивает с ног {character_name}. Он ломает кости и становиться уязвим.")
                await message.answer(f"Грахогмот наносит {damage} урона. Теперь жизненные силы {character_name} {character_hp}/{character_max_hp}.")
                if character_hp <= 0:
                    await message.answer("Вы умерли!")
                    return
                else:
                    pass


@dp.message_handler(text='💥Навыки💥')
async def handle_exercises(message: types.Message):
    if player_choosing_move_istrue == True:
        player_choosing_move_istrue = False
        await message.answer("Ты выбрал Навыки!")


@dp.message_handler(text='🧪Предметы🧪')
async def handle_formulas(message: types.Message):
    if player_choosing_move_istrue == True:
        player_choosing_move_istrue = False
        await message.answer("Ты выбрал Предметы!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
