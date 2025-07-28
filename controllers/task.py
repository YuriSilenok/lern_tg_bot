"""Модуль содержит логику для задач"""

from typing import Any, Dict, List

from models.task import Task
from models.theme import Theme


def get_tasks(theme_id: int) -> List[Dict[str, Any]]:
    """Вернуть список задач темы"""

    theme = Theme.get_or_none(id=theme_id)
    if theme is None:
        raise ValueError(f'Тема не с id={theme_id} найдена')
    
    return [
        dict(task) for task in Task.select().where(Task.theme == theme)
    ]