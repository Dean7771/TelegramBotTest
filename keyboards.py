from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог111")],
        [KeyboardButton(text="Контакты"), KeyboardButton(text="Корзина")]
    ], resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню!"
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Nike", callback_data='brand_nike')],
        [InlineKeyboardButton(
            text="Adidas", callback_data='brand_adidas')],
        [InlineKeyboardButton(
            text="Reebok", callback_data='brand_reebok')]
    ]
)

get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отравить номер", request_contact=True)]
    ], resize_keyboard=True
)
