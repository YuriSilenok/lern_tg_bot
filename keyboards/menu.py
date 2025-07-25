from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from filters.permission import IsPermission
from models.user import User

def get_keyboard(user_tg_id: int):
    """Получить меню пользователя"""

    user = User.get_or_none(tg_id=user_tg_id)

    add_course_permission = IsPermission(permission_name='Добавить курс')

    keyboard = []
    first_row = []

    if add_course_permission.check(user=user):
        first_row.append(KeyboardButton(text='Добавить курс'))

    first_row.append(KeyboardButton(text='Мои курсы'))

    keyboard.append(first_row)

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
