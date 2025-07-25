from aiogram.fsm.state import StatesGroup, State

class AddCourseState(StatesGroup):

    input_course_name = State()