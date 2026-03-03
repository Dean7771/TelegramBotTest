from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart, Command
from datetime import datetime
import keyboards as kb
from states import Reg

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Здравствуйте, рады Вас приветствовать в своем клубе.\n\nВведите ваше имя", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reg.name)


@user.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отправьте ваш номер телефона", reply_markup=kb.get_number)
    await state.set_state(Reg.number)


@user.message(Reg.number, F.contact)
async def reg_contact(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)

    data = await state.get_data()
    await message.answer(f"Вы зарегистрировались! \n\n Имя: {data["name"]} \n Номер: {data["phone"]}", reply_markup=kb.menu)
    await state.clear()


@user.message(Reg.number)
async def reg_contact(message: Message, state: FSMContext):
    await message.answer("Отправьте контакт по кнопке ниже!", reply_markup=kb.get_number)


@user.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Вы написали команду /help")


@user.message(Command('time'))
async def cmd_time(message: Message):
    time = datetime.now()
    await message.answer("Текущее время: " + str(time.strftime("%H:%M:%S")))


@user.message(F.text == "Каталог")
async def cmd_catalog(message: Message):
    await message.answer("Вы выбрали каталог!",
                         reply_markup=kb.catalog)


@user.callback_query(F.data.startswith('brand_'))
async def cheak_brand(callback: CallbackQuery):
    brand_name = callback.data.split("_")[1]
    await callback.answer("Бренд")
    await callback.message.answer(f"Вы выбрали {brand_name.capitalize()}")


@user.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f"Вы прислали фото!\n\nЕго id: {message.photo[-1].file_id}")
    await message.answer_photo(photo=message.photo[-2].file_id)


@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)
