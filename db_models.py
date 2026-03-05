from datetime import datetime
from typing import Optional

from sqlalchemy import String, func, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Teacher(Base):
    __tablename__ = 'teachers'

    id : Mapped[int] = mapped_column(primary_key=True , index=True )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email : Mapped[str] = mapped_column(String(255) , unique=True , nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now()
    )

    profile: Mapped[Optional["TeacherProfile"]] = relationship(
        back_populates="teacher",
        uselist=False,                      #uselist refer 1 to  1 relationship teachers only have one teacher profile
        cascade="all, delete-orphan",       #study orm cascade types,
        lazy="joined"                       #lazy="joined" mean set loading to eager loading
    )

