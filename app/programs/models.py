import uuid
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    Table,
    DateTime,
    Enum as SqlALchemyEnum,
    Text,
    Column,
    ForeignKey,
    Integer
)
from providers.database import Base
from typing import List
from datetime import datetime

class StatusProgram(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class TypeProgram(str, Enum):
    TECHNICIAN = "TECHNICIAN"
    TECHNOLOGIST = "TECHNOLOGIST"
    UNDERGRADUATE = "UNDERGRADUATE"
    POSTGRADUATE = "POSTGRADUATE"

class Program(Base):
    __tablename__ = "programs"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    type: Mapped[str] = mapped_column(SqlALchemyEnum(TypeProgram), nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    certificate: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(SqlALchemyEnum(StatusProgram), nullable=False, default=StatusProgram.ACTIVE)
    timing_system: Mapped[str] = mapped_column(String(100), nullable=False)

    # Add groups relationship
    groups: Mapped[List["Group"]] = relationship(back_populates="program")
