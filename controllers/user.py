import functools


def validate(func):
    """Валидирует пользователя и передает модель пользователя в функцию"""
    
    @functools.wraps(func)
    async def wrapper(*args, **qwargs):