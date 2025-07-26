"""Запуститье этот модуль для создания таблиц и данных"""

from models.connect import db
from models.course import Course
from models.theme import Theme
from models.user import User
from models.role import Role
from models.user_role import UserRole
from models.permission import Permission
from models.role_permission import RolePermission


def create_tables() -> None:
    """СОздает таблицы и данные"""
    db.connect()
    db.create_tables(
        models=[
            Course,
            Theme,
            User,
            Role,
            UserRole,
            Permission,
            RolePermission,
        ],
        safe=True,
    )
    db.close()


def cretae_permission() -> None:
    """Создает роли, привелегии, распределяем роли и привилегии"""

    userroles = [(320720102, "Преподаватель")]

    for tg_id, role_name in userroles:
        UserRole.get_or_create(
            role=Role.get_or_create(name=role_name)[0],
            user=User.get_or_create(tg_id=tg_id)[0],
        )

    rolepermissions = [
        ("Преподаватель", "Мои курсы"),
        ("Преподаватель", "Добавить курс"),
        ("Преподаватель", "Просмотр тем курса"),
        ("Преподаватель", "Добавить тему"),
    ]

    for role_name, permission_name in rolepermissions:
        RolePermission.get_or_create(
            role=Role.get_or_create(name=role_name)[0],
            permission=Permission.get_or_create(name=permission_name)[0],
        )


if __name__ == "__main__":
    create_tables()
    cretae_permission()
