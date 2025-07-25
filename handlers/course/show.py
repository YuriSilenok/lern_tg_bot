"""Модуль добавления преподавателем курса"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

import keyboards
from filters.permission import IsPermission


router = Router()


@router.message(
    F.text == "Мои курсы",
    IsPermission(permission_name="Мои курсы"),
)
async def show_courses_handler(message: Message):
    """Обработчик сообщения Мои курсы"""

    try:
        await message.answer(
            text="Ваши курсы",
            reply_markup=keyboards.course.get_kb(
                user_tg_id=message.from_user.id
            ),
        )
    except TelegramBadRequest as ex:
        print("show_courses_handler", message.from_user.id, ex)
    except ValueError as ex:
        await message.answer(text=ex)
