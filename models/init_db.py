"""Запуститье этот модуль для создания таблиц и данных"""

import models


def create_tables() -> None:
    """СОздает таблицы и данные"""
    models.db.connect()
    models.db.create_tables(
        models=[
            models.Course,
            models.Test,
            models.Theme,
            models.User,
            models.Role,
            models.Task,
            models.UserRole,
            models.Permission,
            models.RolePermission,
        ],
        safe=True,
    )
    models.db.close()


def cretae_permission() -> None:
    """Создает роли, привелегии, распределяем роли и привилегии"""

    userroles = [(320720102, "Преподаватель")]

    for tg_id, role_name in userroles:
        models.UserRole.get_or_create(
            role=models.Role.get_or_create(name=role_name)[0],
            user=models.User.get_or_create(tg_id=tg_id)[0],
        )

    rolepermissions = [
        ("Преподаватель", "Мои курсы"),
        ("Преподаватель", "Добавить курс"),
        ("Преподаватель", "Просмотр тем курса"),
        ("Преподаватель", "Добавить тему"),
        ("Преподаватель", "Просмотр тестов темы"),
        ("Преподаватель", "Просмотр задач темы"),
        ("Преподаватель", "Просмотр списка групп"),
    ]

    for role_name, permission_name in rolepermissions:
        models.RolePermission.get_or_create(
            role=models.Role.get_or_create(name=role_name)[0],
            permission=models.Permission.get_or_create(name=permission_name)[
                0
            ],
        )


if __name__ == "__main__":
    create_tables()
    cretae_permission()
