"""Обработчики для добавления варианта ответа"""

from aiogram import Router, F
from aiogram.types import ContentType, Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from controllers.answer import add_answer, get_answer_by_id, set_answer
from controllers.question import get_question_by_id
from filters.permission import IsPermission
from keyboards.answer import get_answer_kb
from keyboards.question import get_question_kb
from states.answer import AddAnswerState

router = Router()

@router.message(
    AddAnswerState.input_text,
    IsPermission(permission_name="Добавить вопрос"),
    F.content_type == ContentType.TEXT,
)
async def input_answer_text_handler(message: Message, state: FSMContext) -> None:
    """Обработка ввода текста варианта ответа на вопрос"""

    data = await state.get_data()
    question = data['question']
    answer = add_answer(question_id=question["id"], text=message.text)
    await message.answer(
        text="Этот вариант ответа верный?",
        reply_markup=get_answer_kb(answer_id=answer["id"]),
    )
    await state.set_state()


@router.callback_query(
    F.data.startswith("answer_yes_"),
    IsPermission(permission_name="Добавить вопрос"),
)
async def set_answer_is_valid_true_handler(callback: CallbackQuery, state: FSMContext):
    """Обработка установки истиности варианта ответа"""

    try:
        answer_id = int(callback.data.split(sep="_")[-1])
        answer = get_answer_by_id(answer_id=answer_id)
        question = answer['question']
        set_answer(answer_id=answer_id, is_valid=True)
        await callback.message.answer(
            text=(
                f"Ответ '{answer['text']}' записан как правильный "
                f"для вопроса '{question['text']}'"
            ),
            reply_markup=get_question_kb(question_id=question["id"])
        )

    except TelegramBadRequest as ex:
        print("set_answer_is_valid_true_handler", callback.from_user.id, ex)

    except ValueError as ex:
        await callback.answer(text=ex)

    await state.clear()
    await callback.message.delete()

@router.callback_query(
    F.data.startswith("answer_no_"),
    IsPermission(permission_name="Добавить вопрос"),
)
async def set_answer_is_valid_false_handler(callback: CallbackQuery, state: FSMContext):
    """Обработка установки истиности варианта ответа"""

    try:
        answer_id = int(callback.data.split(sep="_")[-1])
        answer = get_answer_by_id(answer_id=answer_id)
        question = answer["question"]
        set_answer(answer_id=answer_id, is_valid=False)
        await callback.message.answer(
            text=(
                f"Ответ '{answer['text']}' записан как неправильный "
                f"для вопроса '{question['text']}'"
            ),
            reply_markup=get_question_kb(question_id=question["id"])
        )

    except TelegramBadRequest as ex:
        print("set_answer_is_valid_false_handler", callback.from_user.id, ex)

    except ValueError as ex:
        await callback.answer(text=ex)

    await state.clear()
    await callback.message.delete()

@router.callback_query(
    F.data.startswith("add_answer_"),
    IsPermission(permission_name="Добавить вопрос"),
)
async def add_answer_handler(callback: CallbackQuery, state: FSMContext):
    """Обработка кнопки добавить вариант ответа"""

    question_id = int(callback.data.split(sep="_")[-1])
    await callback.message.answer(
        text="Введите текст варианта ответа."
    )
    await state.set_state(state=AddAnswerState.input_text)
    await state.update_data(
        question=get_question_by_id(question_id=question_id)
    )
    await callback.message.delete()
    
    