"""Добавление роутеров"""

from aiogram import Dispatcher

from . import commands
from . import course
from . import theme
from . import test
from . import task


def add_routers(dp: Dispatcher) -> None:
    """Добавляет роутеры в диспетчер"""

    commands.add_routers(dp=dp)
    course.add_routers(dp=dp)
    theme.add_routers(dp=dp)
    test.add_routers(dp=dp)
    task.add_routers(dp=dp)
