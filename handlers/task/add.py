"""Модуль добавления преподавателем задачи в тему"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from controllers.question import add_question
from controllers.task import add_task
from filters.permission import IsPermission
from keyboards.question import get_question_kb
from keyboards.task import get_tasks_kb
from states.answer import AddAnswerState
from states.question import AddQuestionState
from states.task import AddTaskState

router = Router()


@router.callback_query(
    F.data.startswith("add_task_"),
    IsPermission(permission_name="Добавить задачу"),
)
async def add_task_handler(callback: CallbackQuery, state: FSMContext):
    """Обработка добавления задачи в тему"""

    try:
        theme_id = int(callback.data.split(sep="_")[-1])
        await callback.message.answer(text="Введите название задачи")
        await state.set_state(state=AddTaskState.input_title)
        await state.update_data(theme_id=theme_id)
        await callback.message.delete_reply_markup()

    except TelegramBadRequest as ex:
        print("add_task_handler", callback.from_user.id, ex)

    except ValueError as ex:
        await callback.answer(text=ex)


@router.message(
    AddTaskState.input_title,
    IsPermission(permission_name="Добавить задачу"),
    F.content_type == ContentType.TEXT,
)
async def input_task_title_handler(message: Message, state: FSMContext):
    """Обработка ввода названия задачи"""

    try:
        await state.update_data(task_title=message.text)
        await state.set_state(state=AddTaskState.input_url)
        await message.answer(text="Введите url текста задачи")

    except TelegramBadRequest as ex:
        print("input_task_title_handler", message.from_user.id, ex)

    except ValueError as ex:
        await message.answer(text=ex)


@router.message(
    AddTaskState.input_url,
    IsPermission(permission_name="Добавить задачу"),
    F.content_type == ContentType.TEXT,
)
async def input_task_url_handler(message: Message, state: FSMContext) -> None:
    """Обработка ввода url темы"""

    data = await state.get_data()
    theme_id = data["theme_id"]
    task_title = data["task_title"]
    add_task(theme_id=theme_id, title=task_title, url=message.text)
    await message.answer(
        text=f"Задача '{task_title}' добавлена",
        reply_markup=get_tasks_kb(theme_id=theme_id),
    )
    await state.clear()
