from aiogram import Router, F, types

group_router = Router()
restricted_words = ["какашка", "лох","дуралей","дебил","глупый","не хороший человек","вонючка"]


@group_router.message(F.text)
async def cleaner(message: types.Message):
    word_list = message.text.split(" ")
    for word in word_list:
        if word.lower() in restricted_words:
            await message.delete()
            break
