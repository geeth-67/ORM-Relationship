from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database_config import get_db
from response_model import StudentResponse, StudentCreate
from student_repository import StudentRepository


router = APIRouter(prefix="/student", tags=["Student Endpoints"])

@router.post("/student" , response_model=StudentResponse , status_code=status.HTTP_201_CREATED)
async def create_student(data: StudentCreate , db: AsyncSession= Depends(get_db)):

    repo = StudentRepository(db)
    student = await repo.create(data)
    return student