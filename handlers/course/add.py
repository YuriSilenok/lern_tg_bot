"""Модуль добавления преподавателем курса"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from controllers.course import add_course
from filters.permission import IsPermission
from keyboards.course import get_courses_kb
from states.course import AddCourseState

router = Router()


@router.callback_query(
    F.data == "add_course",
    IsPermission(permission_name="Добавить курс"),
)
async def add_course_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки Добавить курс"""

    try:
        await callback.message.answer(text="Введите название курса")
    except TelegramBadRequest as ex:
        print("add_course_handler", callback.from_user.id, ex)
    except ValueError as ex:
        await callback.answer(text=ex)

    await state.set_state(state=AddCourseState.input_title)


@router.message(
    AddCourseState.input_title,
    IsPermission(permission_name="Добавить курс"),
    F.content_type == ContentType.TEXT,
)
async def input_course_title_handler(
    message: Message, state: FSMContext
) -> None:
    """Обрабатываем ввод названия курса"""

    try:
        add_course(title=message.text, user_tg_id=message.from_user.id)
        await message.answer(
            text=f"Курс '{message.text}' создан",
            reply_markup=get_courses_kb(user_tg_id=message.from_user.id)
        )
        await state.clear()
    except TelegramBadRequest as ex:
        print("input_course_name_handler", message.from_user.id, ex)
    except ValueError as ex:
        await message.answer(text=ex)
