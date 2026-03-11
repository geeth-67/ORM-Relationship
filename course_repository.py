from sqlalchemy.ext.asyncio import AsyncSession

from db_models import Courses
from response_model import CourseCreate


class CourseRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: CourseCreate) -> Courses:
        course = Courses(name=data.name, email=data.email)

        self.db.add(course)
        await self.db.commit()
        await self.db.refresh(course)
        return course