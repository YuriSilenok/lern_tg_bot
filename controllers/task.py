"""Модуль содержит логику для задач"""

from typing import Any, Dict, List

from models.task import Task
from models.theme import Theme


def add_task(theme_id: int, title: str, url: str) -> Dict[str, Any]:
    """Добавить задачу в тему"""

    theme = Theme.get_or_none(id=theme_id)
    if theme is None:
        raise ValueError(f"Тема не с id={theme_id} найдена")
    
    task, created = Task.get_or_create(
        theme=theme,
        title=title,
        url=url,
    )

    if not created:
        raise ValueError(f"Задача '{title}' Вами уже ранее создавалась.")

    return dict(task)

def get_tasks(theme_id: int) -> List[Dict[str, Any]]:
    """Вернуть список задач темы"""

    theme = Theme.get_or_none(id=theme_id)
    if theme is None:
        raise ValueError(f"Тема не с id={theme_id} найдена")

    return [dict(task) for task in Task.select().where(Task.theme == theme)]
