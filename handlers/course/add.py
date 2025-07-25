"""Модуль добавления преподавателем курса"""

from aiogram import Router, F
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from controllers.course import add_course
from filters.permission import IsPermission
from states.course.add import AddCourseState

router = Router()

@router.message(
        F.text == 'Добавить курс',
        IsPermission(permission_name="Добавить курс"),
)
async def add_course_handler(message: Message, state: FSMContext):
    """Обработчик сообщения Добавить курс"""

    try:
        await message.answer(text="Введите название курса")
    except TelegramBadRequest as ex:
        print('add_course_handler', message.from_user.id, ex)
    except ValueError as ex:
        await message.answer(text=ex)

    await state.set_state(state=AddCourseState.input_course_name)

@router.message(
    AddCourseState.input_course_name,
    IsPermission(permission_name="Добавить курс"),
    F.content_type == ContentType.TEXT,
)
async def input_course_name_handler(message: Message, state: FSMContext) -> None:
    """Обрабатываем ввод названия курса"""

    try:
        add_course(name=message.text, user_tg_id=message.from_user.id)
        await message.answer(text="Курс создан")
        await state.clear()
    except TelegramBadRequest as ex:
        print('input_course_name_handler', message.from_user.id, ex)
    except ValueError as ex:
        await message.answer(text=ex)