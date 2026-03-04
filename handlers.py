from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
import keyboards as kb
from states import Reg
from generate import ai_generate, ai_get_balanc

user = Router()


class Gen(StatesGroup):
    wait = State()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет, напиши свой запрос.", reply_markup=kb.menu)


@user.message(Command('balance'))
async def balancenow(message: Message):
    balance = await ai_get_balanc()
    await message.answer(f"✅ Текущий баланс: {balance} USD")


@user.message(F.text == "Прервать запрос!")
async def cmd_stop(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Напишите новый запрос")


@user.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подожди, ответ генерируется!")


@user.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response)
    await state.clear()
