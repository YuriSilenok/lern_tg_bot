from aiogram import Dispatcher

from . import commands
from . import course


def add_routers(dp: Dispatcher) -> None:
    """Добавляет роутеры в диспетчер"""

    commands.add_routers(dp=dp)
    course.add_routers(dp=dp)
