"""Модуль добавления преподавателем темы в курс"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from controllers.theme import add_theme
from filters.permission import IsPermission
from states.theme import AddThemeState

router = Router()


@router.callback_query(
    F.data.startswith("add_theme_"),
    IsPermission(permission_name="Добавить тему"),
)
async def add_theme_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки Добавить тему"""

    try:
        course_id = int(callback.data.split(sep="_")[-1])
        await state.update_data(course_id=course_id)
        await callback.message.answer(text="Введите название темы")

    except TelegramBadRequest as ex:
        print("add_theme_handler", callback.from_user.id, ex)

    except ValueError as ex:
        await callback.answer(text=ex)

    await state.set_state(state=AddThemeState.input_title)


@router.message(
    AddThemeState.input_title,
    IsPermission(permission_name="Добавить тему"),
    F.content_type == ContentType.TEXT,
)
async def input_theme_title_handler(
    message: Message, state: FSMContext
) -> None:
    """Обрабатываем ввод названия курса"""

    try:
        await state.update_data(theme_title=message.text)
        await state.set_state(state=AddThemeState.input_url)
        await message.answer(text="Введите url на материалы темы")
    except TelegramBadRequest as ex:
        print("input_theme_name_handler", message.from_user.id, ex)

    except ValueError as ex:
        await message.answer(text=ex)


@router.message(
    AddThemeState.input_url,
    IsPermission(permission_name="Добавить тему"),
    F.content_type == ContentType.TEXT,
)
async def input_theme_url_handler(message: Message, state: FSMContext) -> None:
    """Обработка ввода url темы"""

    data = await state.get_data()
    course_id = data["course_id"]
    theme_title = data["theme_title"]
    add_theme(course_id=course_id, title=theme_title, url=message.text)
    await message.answer(text="Тема добавлена")
    await state.clear()
