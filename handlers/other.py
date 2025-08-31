"""Обработка всего необработанного"""

from aiogram import Router
from aiogram.types import CallbackQuery, Message


router = Router()


@router.callback_query()
async def other_callback_handler(callback: CallbackQuery):
    """Обработчик необработаных нажатий кнопок"""

    await callback.answer(text=callback.data)


@router.message()
async def other_callback_handler(message: Message):
    """Обработчик необработаных нажатий кнопок"""

    await message.answer(text=f"Нет обработчкиа на сообщение '{message.text}'")
