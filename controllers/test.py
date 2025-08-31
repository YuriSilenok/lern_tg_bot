"""Модуль содержит логику для тестов"""

from peewee import fn, JOIN

from models.course import Course
from models.question import Question
from models.theme import Theme
from models.user import User
from models.user_question import UserQuestion
from models.user_theme import UserTheme


def generate_test(user_tg_id: int, course_id: int):
    """Генерация теста по курсу для пользователя"""

    user = User.get_or_none(tg_id=user_tg_id)
    if user is None:
        raise ValueError(f"Пользователь с tg_id={user_tg_id} не найден")

    course = Course.get_or_none(id=course_id)
    if course is None:
        raise ValueError(f"Курс с id={course_id} не найден")

    # получаем список вопросов из освоеных пользователем тем по курсу
    list(
        Question.select(
            Question.id,
            Question.text,
            fn.COALESCE(UserQuestion.score, 0).alias("score"),
        )
        .join(
            UserTheme,
            on=(
                (Question.theme == UserTheme.theme)
                & (UserTheme.user == user.id)
            ),
        )
        .join(
            Theme, on=((Theme.id == UserTheme) & (Theme.course == course.id))
        )
        .join(
            UserQuestion,
            JOIN.LEFT_OUTER,
            on=(
                (Question.id == UserQuestion.question_id)
                & (UserQuestion.user_id == user.id)
            ),
        )
        .order_by(fn.COALESCE(UserQuestion.score, 0).alias("score"))
    )

    # ближайшая неосвоенная тема
    wip_theme = (
        Theme.select()
        .where(
            (Theme.course == course.id)
            & (
                ~Theme.id
                << (
                    Theme.select(Theme.id)
                    .join(UserTheme, on=Theme.id == UserTheme.theme)
                    .where(Theme.course == course.id)
                )
            )
        )
        .first()
    )
    list(Question.select().where(Question.theme == wip_theme.id))


if __name__ == "__main__":
    generate_test(user_tg_id=320720102, course_id=1)
