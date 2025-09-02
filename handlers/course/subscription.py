"""Модуль добавления подписки и отписки на от курса"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from keyboards.course import get_my_courses_kb
from keyboards.course import get_all_courses_kb
from filters.permission import IsPermission


router = Router()
