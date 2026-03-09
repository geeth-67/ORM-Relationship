from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db_models import Teacher, TeacherProfile
from response_model import TeacherCreate


class TeacherRepository:

    def __init__(self , db: AsyncSession):
        self.db = db

    async def create(self, data: TeacherCreate) -> Teacher:
        teacher = Teacher(name=data.name, email=data.email)

        if data.profile:
            teacher.profile = TeacherProfile(**data.profile.model_dump())

        try:
            self.db.add(teacher)
            await self.db.commit()
            await self.db.refresh(teacher)
            return teacher
        except IntegrityError:
            await self.db.rollback()
            raise HTTPException(
                status_code=409,
                detail=f"A teacher with email '{data.email}' already exists."
            )