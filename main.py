from aiogragm import Bot, Dispatcher
import asyncio

from handlers.user_private import user_router
from handlers.user_group import group_router
bot = Bot(token='8638415155:AAH6Bt8XzkiGWvfZa4HUsieFceWhx0VWHEI')
dp = Dispatcher()
dp.include_router(user_router)
dp.include_router(group_router)
async def main():
    print('bot ushel')
    await dp.start_polling(bot)


asyncio.run(main())
