"""Добавление роутеров"""

from aiogram import Dispatcher

from . import commands
from . import course
from . import theme
from . import question
from . import answer
from . import task
from . import other


def add_routers(dp: Dispatcher) -> None:
    """Добавляет роутеры в диспетчер"""

    commands.add_routers(dp=dp)
    course.add_routers(dp=dp)
    theme.add_routers(dp=dp)
    question.add_routers(dp=dp)
    task.add_routers(dp=dp)
    answer.add_routers(dp=dp)
    dp.include_routers(other.router)
