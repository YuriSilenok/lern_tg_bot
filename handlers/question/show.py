"""Показать список тестов в теме"""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from controllers.question import get_question_by_id
from controllers.theme import get_theme_by_id
from filters.permission import IsPermission
from keyboards.question import get_question_kb, get_questions_kb


router = Router()


@router.callback_query(
    F.data.startswith("questions_theme_"),
    IsPermission(permission_name="Просмотр вопросов"),
)
async def show_questions_handler(callback: CallbackQuery) -> None:
    """Просмотр списка тестов темы"""

    theme_id = int(callback.data.split(sep="_")[-1])
    theme = get_theme_by_id(theme_id=theme_id)

    await callback.message.answer(
        text=f'Вопросы по теме: {theme["title"]}',
        reply_markup=get_questions_kb(theme_id=theme_id),
    )
    await callback.message.delete_reply_markup()


@router.callback_query(
    F.data.startswith("question_"),
    IsPermission(permission_name="Просмотр вопросов"),
)
async def show_question_handler(callback: CallbackQuery) -> None:
    """Просмотр вопроса"""

    question_id = int(callback.data.split(sep="_")[-1])
    question = get_question_by_id(question_id=question_id)

    await callback.message.answer(
        text=f'Варианты ответов на вопрос: {question["text"]}',
        reply_markup=get_question_kb(question_id=question_id),
    )
    await callback.message.delete_reply_markup()
