"""Показать список тем курса"""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from controllers.answer import get_answer_by_id
from filters.permission import IsPermission
from keyboards.answer import get_answer_kb


router = Router()


@router.callback_query(
    F.data.startswith("answer_"),
    IsPermission(permission_name="Просмотр вопросов"),
)
async def show_answer_handler(callback: CallbackQuery) -> None:
    """Показать вариант ответа"""

    answer_id = int(callback.data.split(sep="_")[-1])
    answer = get_answer_by_id(answer_id=answer_id)

    await callback.message.answer(
        text=f"Вариант ответа: {answer['text']}",
        reply_markup=get_answer_kb(answer_id=answer_id),
    )
    await callback.message.delete_reply_markup()
