from models.connect import db
from models.course import Course
from models.theme import Theme
from models.user import User
from models.role import Role
from models.user_role import UserRole
from models.permission import Permission
from models.role_permission import RolePermission


def initialize_database():
    db.connect()
    db.create_tables(
        models=[
            Course,
            Theme,
            User,
            Role,
            UserRole,
            Permission,
            RolePermission,
        ],
        safe=True,
    )
    db.close()
    teacher_role, _ = Role.get_or_create(name="Преподаватель")
    teacher, _ = User.get_or_create(tg_id=320720102)
    UserRole.get_or_create(
        role=teacher_role,
        user=teacher,
    )

    add_course_permission, _ = Permission.get_or_create(name="Добавить курс")
    show_courses_permission, _ = Permission.get_or_create(name="Мои курсы")

    RolePermission.get_or_create(
        role=teacher_role,
        permission=add_course_permission,
    )
    RolePermission.get_or_create(
        role=teacher_role,
        permission=show_courses_permission,
    )


if __name__ == "__main__":
    initialize_database()
