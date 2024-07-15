from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


start_router: Router = Router()

@start_router.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer("Salom xush kelibsiz!")
