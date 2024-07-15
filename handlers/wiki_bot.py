from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from wiki import wiki_bot

wiki_router: Router = Router()

@wiki_router.message()
async def wiki_handler(msg:Message):
    await msg.answer(wiki_bot(msg.text))