from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("""ПРИВИТ МОЙ БОТ МОЖЕТ СЬЕСТЬ ТВОЕГО ХОМЯЧКА
    /info - информация о боте
    /search - поиск музыки
    /pudge - СЕКРЕТ""")


# @user_router.message()
# async def echo(message: types.Message):
#     answer = message.text
#     await message.answer(answer)


@user_router.message(Command('info'))
async def info(message: types.message):
    await message.answer('тут была-бы ваша реклама')


@user_router.message(Command('search'))
async def search(message: types.message):
   await message.answer('рамштайн нэвэр дай')


@user_router.message(Command('pudge'))
async def pudge(message: types.message):
    await message.answer('PUDGE PUDGE PUDGE PUDGE!!!')