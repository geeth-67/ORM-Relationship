from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db_models import Courses, Student
from response_model import CourseCreate


class CourseRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: CourseCreate) -> Courses:
        course = Courses(name=data.name,
                         code=data.code,
                         description=data.description,
                         credits=data.credits,
                         is_active=data.is_active,)

        if data.student_id:
            students = await self.get_students(data.student_ids)
            course.students = students
        self.db.add(course)
        await self.db.commit()
        await self.db.refresh(course)
        return course

    async def get(self, student_ids) -> Courses:
        query =select(Student).where(Student.id == id)