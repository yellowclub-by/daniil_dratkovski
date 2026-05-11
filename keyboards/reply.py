from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=
    [
        [KeyboardButton(text="поиск музыки"), KeyboardButton(text="информация о боте")],
        [KeyboardButton(text='донат')]
    ],resize_keyboard=True,input_field_placeholder='biba'
)

start_kb = ReplyKeyboardMarkup(
    keyboard=   [
        [KeyboardButton(text='Старт')]
    ]
)

search_kb = ReplyKeyboardMarkup(
    keyboard=   [
        [KeyboardButton(text='пoиск по звуку')],[KeyboardButton(text='пoиск по тексту')],
        [KeyboardButton(text='п0иск по композитору')]
    ]
)