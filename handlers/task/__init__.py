"""Добавление роутеров"""

from aiogram import Dispatcher

from . import show


def add_routers(dp: Dispatcher) -> None:
    """Добавляет роутеры в диспетчер"""

    dp.include_routers(show.router)
