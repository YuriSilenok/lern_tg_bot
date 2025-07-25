"""Обработка команды start"""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest

from keyboards.menu import get_keyboard


router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    """Обработчик команды start"""

    try:
        await message.answer(
            text=(
                "Вы запустили бота для дистанционного изучения "
                "программирования"
            ),
            reply_markup=get_keyboard(user_tg_id=message.from_user.id),
        )
    except TelegramBadRequest as ex:
        print("add_course_handler", message.from_user.id, ex)
    except ValueError as ex:
        await message.answer(text=ex)
