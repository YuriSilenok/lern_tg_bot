"""Библиотеки для проверки пользователя"""

from aiogram.filters import BaseFilter
from aiogram.types import Message
from models import User, UserRole, Role


class IsRole(BaseFilter):
    """Проверяет наличие привелегии у пользователя"""

    def __init__(self, role_name: str = None) -> None:
        self.role = (
            Role.get(name=role_name) if role_name else None
        )

    def check(self, user_tg_id: int) -> bool:
        """Проверяет у пользователя привелегию"""

        user: User = User.get_or_none(tg_id=user_tg_id)

        if user is None:
            return False

        role: Role = (
            UserRole.select()
            .where(
                (UserRole.user == user)
                & (UserRole.role == self.role)
            )
            .first()
        )
        return role is not None

    async def __call__(self, message: Message) -> bool:
        return self.check(user_tg_id=message.from_user.id)
