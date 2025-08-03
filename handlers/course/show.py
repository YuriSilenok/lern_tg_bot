"""Модуль добавления преподавателем курса"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from keyboards.course import get_courses_kb
from filters.permission import IsPermission


router = Router()


@router.message(
    F.text == "Мои курсы",
    IsPermission(permission_name="Просмотр курсов"),
)
async def show_courses_message_handler(message: Message) -> None:
    """Обработчик сообщения Мои курсы"""

    try:
        await message.answer(
            text="Ваши курсы",
            reply_markup=get_courses_kb(user_tg_id=message.from_user.id),
        )
    except TelegramBadRequest as ex:
        print("show_courses_message_handler", message.from_user.id, ex)
    except ValueError as ex:
        await message.answer(text=ex)


@router.callback_query(
    F.data == "courses",
    IsPermission(permission_name="Просмотр курсов"),
)
async def show_courses_callback_handler(callback: CallbackQuery) -> None:
    """Обработчик сообщения Мои курсы"""

    try:
        await callback.message.answer(
            text="Ваши курсы",
            reply_markup=get_courses_kb(user_tg_id=callback.from_user.id),
        )
    except TelegramBadRequest as ex:
        print("show_courses_callback_handler", callback.from_user.id, ex)
    except ValueError as ex:
        await callback.answer(text=ex)
    await callback.message.delete_reply_markup()
