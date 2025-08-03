"""Модуль добавления преподавателем темы в курс"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from controllers.question import add_question
from filters.permission import IsPermission
from keyboards.question import get_question_kb
from states.answer import AddAnswerState
from states.question import AddQuestionState

router = Router()


@router.callback_query(
    F.data.startswith("add_question_"),
    IsPermission(permission_name="Добавить вопрос"),
)
async def add_question_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки Добавить вопрос"""

    try:
        theme_id = int(callback.data.split(sep="_")[-1])
        await state.update_data(theme_id=theme_id)
        await callback.message.answer(text="Введите текст вопроса")

    except TelegramBadRequest as ex:
        print("add_question_handler", callback.from_user.id, ex)

    except ValueError as ex:
        await callback.answer(text=ex)

    await state.set_state(state=AddQuestionState.input_text)
    await callback.message.delete_reply_markup()


@router.message(
    AddQuestionState.input_text,
    IsPermission(permission_name="Добавить вопрос"),
    F.content_type == ContentType.TEXT,
)
async def input_question_text_handler(
    message: Message, state: FSMContext
) -> None:
    """Обработка ввода текста вопроса"""

    try:
        data = await state.get_data()
        theme_id = data["theme_id"]
        question = add_question(theme_id=theme_id, text=message.text)
        data["question"] = question
        data["answers"] = []
        await message.answer(
            text=(
                f"Вопрос с текстом '{question['text']}' добавлен. "
                "Введите текст варианта ответа."
            ),
            reply_markup=get_question_kb(question_id=question["id"]),
        )
        await state.set_data(data=data)
        await state.set_state(state=AddAnswerState.input_text)

    except TelegramBadRequest as ex:
        print("input_question_text_handler", message.from_user.id, ex)

    except ValueError as ex:
        await message.answer(text=ex)
