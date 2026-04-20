from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("""ПРИВИТ МОЙ БОТ МОЖЕТ СЬЕСТЬ ТВОЕГО ХОМЯЧКА
    /info - информация о боте
    /search - поиск музыки
    /pudge - СЕКРЕТ""")

 # @user_router.message(F.text)
 # async def image(message: types.message):
 #     await message.answer('omagad')
@user_router.message(Command('info'))
async def info(message: types.message):
    await message.answer('тут была-бы ваша реклама')


@user_router.message(Command('search'))
async def search(message: types.message):
    await message.answer('рамштайн нэвэр дай')


@user_router.message(Command('pudge'))
async def pudge(message: types.message):
    await message.answer('PUDGE PUDGE PUDGE PUDGE!!!')

# @user_router.message(F.text) # фильтр текста
#@user_router.message(F.image) # фильтр kamtinki
#@user_router.message(F.text.lower() == 'дистивка') # фильтр konkritnigo texsty
#@user_router.message(F.text.lower().contains('Lamosa')) # фильтр po zovderjaniy
@user_router.message(F.text.lower().endswith("?"))
# @user_router.message(F.text.lower().startswith("как"), F.text.lower().endwith("?"))
# @user_router.message(F.text.lower().startswith("как") | F.text.lower().endwith("?"))
async def echo(message: types.Message):
    await message.answer('Limo')
