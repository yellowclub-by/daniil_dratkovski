from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from aiogram.types import reply_markup_union

from keyboards import reply

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("""ПРИВИТ МОЙ БОТ МОЖЕТ СЬЕСТЬ ТВОЕГО ХОМЯЧКА
    /info - информация о боте
    /search - поиск музыки
                         """,reply_markup=reply.start_kb)

@user_router.message(Command('start'))
async def second_start(message: types.message):
    await message.answer
@user_router.message(F.text.lower().endswith('?'))
@user_router.message(F.text.lower().contains('что делает'))
@user_router.message(F.text.lower().contains('инфо'))
@user_router.message(F.text.lower().contains('старт'))
@user_router.message(Command('info'))
async def info(message: types.message):
    await message.answer('тут была-бы ваша реклама', reply_markup=reply.main_kb)


@user_router.message(F.text.lower().contains("иск"))
@user_router.message(F.text.lower().contains('поиск'))
@user_router.message(Command('search'))
async def search(message: types.message):
    await message.answer('рамштайн нэвэр дай',reply_markup=reply.search_kb)

# @user_router.message(F.text) # фильтр текста
# @user_router.message(F.image) # фильтр kamtinki
# @user_router.message(F.text.lower() == 'дистивка') # фильтр konkritnigo texsty
# @user_router.message(F.text.lower().contains('Lamosa')) # фильтр po zovderjaniy
# @user_router.message(F.text.lower().endswith("?"))
# @user_router.message(F.text.lower().startswith("как"), F.text.lower().endwith("?"))
# @user_router.message(F.text.lower().startswith("как") | F.text.lower().endwith("?"))
async def echo(message: types.Message):
    await message.answer('Limosa')

@user_router.message('donate')
@user_router.message(F.text.lower().contains("донат"))
async def donate(message: types.message):
    await message.answer('pls donate')