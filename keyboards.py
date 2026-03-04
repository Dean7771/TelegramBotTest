from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Начать диалог с ИИ")]
    ], resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню!")

get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отравить номер", request_contact=True)]
    ], resize_keyboard=True
)
