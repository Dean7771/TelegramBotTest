from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
import keyboards as kb
from states import Reg
from generate import ai_generate

user = Router()


class Gen(StatesGroup):
    wait = State()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет, напиши свой запрос.")


@user.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подожди, ответ генерируется!")


@user.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response, parse_mode='Markdown')
    await state.clear()
