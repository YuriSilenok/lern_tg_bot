"""Библиотеки для проверки пользователя"""

from datetime import datetime
from aiogram.filters import BaseFilter
from aiogram.types import Message
from models import RolePermission, User, UserRole, Permission


class IsPermission(BaseFilter):
    """Проверяет наличие привелегии у пользователя"""

    def __init__(self, permission_name: str = None) -> None:
        self.permission = (
            Permission.get(name=permission_name) if permission_name else None
        )

    def check(self, user: User) -> bool:
        """Проверяет у пользователя привелегию"""

        permission: Permission = (
            RolePermission.select()
            .join(UserRole, on=UserRole.role == RolePermission.role)
            .where(
                (UserRole.user == user)
                & (RolePermission.permission == self.permission)
            )
            .first()
        )
        return permission is not None

    async def __call__(self, message: Message) -> bool:
        user: User = User.get_or_none(tg_id=message.from_user.id)

        if user is None:
            return False

        return self.check(user=user)