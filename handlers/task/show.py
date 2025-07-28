"""Показать список тестов в теме"""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from controllers.theme import get_theme_by_id
from filters.permission import IsPermission
from keyboards.task import get_tasks_kb


router = Router()


@router.callback_query(
    F.data.startswith("tasks_theme_"),
    IsPermission(permission_name="Просмотр задач темы"),
)
async def show_tasks_handler(callback: CallbackQuery):
    """Просмотр списка задач темы"""

    theme_id = int(callback.data.split(sep="_")[-1])
    theme = get_theme_by_id(theme_id=theme_id)

    await callback.message.answer(
        text=f'Задачи по теме: {theme["title"]}',
        reply_markup=get_tasks_kb(theme_id=theme_id),
    )
