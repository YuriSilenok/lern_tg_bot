"""Показать список тем курса"""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from controllers.course import get_course_by_id
from controllers.theme import get_theme_by_id
from filters.permission import IsPermission
from keyboards.theme import get_themes_kb, get_theme_kb


router = Router()


@router.callback_query(
    F.data.startswith("course_"),
    IsPermission(permission_name="Просмотр тем"),
)
async def show_themes_handler(callback: CallbackQuery) -> None:
    """Показать курс со списком тем"""

    course_id = int(callback.data.split(sep="_")[-1])
    course = get_course_by_id(course_id=course_id)

    await callback.message.answer(
        text=f"Курс: {course['title']}",
        reply_markup=get_themes_kb(course_id=course_id, user_tg_id=callback.from_user.id),
    )
    await callback.message.delete_reply_markup()


@router.callback_query(
    F.data.startswith("theme_"),
    IsPermission(permission_name="Просмотр тем"),
)
async def show_theme_menu_handler(callback: CallbackQuery) -> None:
    """Показать меню для темы"""

    theme_id = int(callback.data.split(sep="_")[-1])
    theme = get_theme_by_id(theme_id=theme_id)

    await callback.message.answer(
        text=f'Тема: {theme["title"]}',
        reply_markup=get_theme_kb(theme_id=theme_id),
    )
    await callback.message.delete_reply_markup()
