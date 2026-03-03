from aiogram import Bot, Dispatcher
from handlers import user


async def main():
    bot = Bot(token="8767067214:AAFAxSlVtCimz2Afwqm8DK1ShdRYyv1iKYQ")
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
