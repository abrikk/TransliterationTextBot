from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.markdown import quote_html


async def start_bot(message: types.Message):
    await message.answer(f"Привет, {quote_html(message.from_user.full_name)}!\n\n"
                         f"Отправь мне текст и я переведу его с кириллицы на латиницу "
                         f"и обратно.")


def register_start(dp: Dispatcher):
    dp.register_message_handler(start_bot, CommandStart())
