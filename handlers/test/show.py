"""Показать список тестов в теме"""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from controllers.theme import get_theme_by_id
from filters.permission import IsPermission
from keyboards.test import get_tests_kb


router = Router()


@router.callback_query(
    F.data.startswith("tests_theme_"),
    IsPermission(permission_name="Просмотр тестов темы"),
)
async def show_tests_handler(callback: CallbackQuery):
    """Просмотр списка тестов темы"""

    theme_id = int(callback.data.split(sep="_")[-1])
    theme = get_theme_by_id(theme_id=theme_id)

    await callback.message.answer(
        text=f'Тесты по теме: {theme["title"]}',
        reply_markup=get_tests_kb(theme_id=theme_id)
    )
    