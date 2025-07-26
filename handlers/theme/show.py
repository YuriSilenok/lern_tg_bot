"""Показать список тем курса"""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from controllers.course import get_course_by_id
from filters.permission import IsPermission
from keyboards.theme import get_kb


router = Router()


@router.callback_query(
    F.data.startswith('course_'),
    IsPermission(permission_name="Просмотр тем курса"),
)
async def show_themes_handler(callback: CallbackQuery) -> None:
    """Показать курс со списком тем"""

    course_id = int(callback.data.split(sep='_')[-1])
    course = get_course_by_id(course_id=course_id)

    await callback.message.answer(
        text=f"Курс: {course['title']}",
        reply_markup=get_kb(course_id=course_id)
    )
