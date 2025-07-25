from aiogram import Dispatcher

from . import add
from . import show


def add_routers(dp: Dispatcher) -> None:
    """Добавляет роутеры в диспетчер"""

    dp.include_routers(add.router)
    dp.include_routers(show.router)
