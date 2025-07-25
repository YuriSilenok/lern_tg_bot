from aiogram import Dispatcher

from . import start


def add_routers(dp: Dispatcher) -> None:
    """Добавляет роутеры в диспетчер"""

    dp.include_routers(start.router)