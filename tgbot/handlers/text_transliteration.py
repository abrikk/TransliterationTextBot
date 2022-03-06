import cyrtranslit
from aiogram import types, Dispatcher
from transliterate import translit


async def transliterate_text(message: types.Message):
    await message.answer(translit(message.text, "ru", reversed=True))
    # await message.answer(cyrtranslit.to_latin(message.text, "ru"))


def register_transliterate_text(dp: Dispatcher):
    dp.register_message_handler(transliterate_text, state="*")
