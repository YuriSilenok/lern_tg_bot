"""Обработка всего необработанного"""

from aiogram import Router
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query()
async def other_callback_handler(callback: CallbackQuery):
    """Обработчик необработаных нажатий кнопок"""

    await callback.answer(text=callback.data)
