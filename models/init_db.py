"""Запуститье этот модуль для создания таблиц и данных"""

import models


def create_tables() -> None:
    """СОздает таблицы и данные"""
    models.db.connect()
    models.db.create_tables(
        models=[
            models.User,
            models.Role,
            models.UserRole,
            models.Permission,
            models.RolePermission,
            models.Course,
            models.Theme,
            models.Question,
            models.Answer,
            models.Task,
            models.Test,
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
        ("Преподаватель", "Просмотр курсов"),
        ("Преподаватель", "Просмотр тем"),
        ("Преподаватель", "Просмотр вопросов"),
        ("Преподаватель", "Просмотр задач"),
        ("Преподаватель", "Просмотр групп"),
        ("Преподаватель", "Добавить курс"),
        ("Преподаватель", "Добавить тему"),
        ("Преподаватель", "Добавить вопрос"),
        ("Преподаватель", "Добавить тест"),
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
