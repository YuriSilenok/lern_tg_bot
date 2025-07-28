"""Модуль содержит логику для тестов"""

from typing import Any, Dict, List

from models.test import Test
from models.theme import Theme


def get_tests(theme_id: int) -> List[Dict[str, Any]]:
    """Вернуть список тестов темы"""

    theme = Theme.get_or_none(id=theme_id)
    if theme is None:
        raise ValueError(f'Тема не с id={theme_id} найдена')
    
    return [
        dict(test) for test in Test.select().where(Test.theme == theme)
    ]