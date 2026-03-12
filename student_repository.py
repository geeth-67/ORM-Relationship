from sqlalchemy.ext.asyncio import AsyncSession

from db_models import Student
from response_model import StudentCreate


class StudentRepository:

    def __init__(self , db: AsyncSession):
        self.db = db

    async def create_student(self, data: StudentCreate) -> Student:
        student = Student(name=data.name,
                          email=data.email,
                          enrollment_year=data.enrollment_year,)

        self.db.add(student)
        await self.db.commit()
        await self.db.refresh(student)
        return student