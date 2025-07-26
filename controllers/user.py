
from models import User


def get_user(tg_id: int) -> dict:
    """Вернут курс"""

    return dict(User.get(tg_id=tg_id))