import uuid
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    DateTime,
    Enum as SqlALchemyEnum,
    Text,
    ForeignKey,
    Table,
    Column
)
from providers.database import Base
from datetime import datetime
from app.programs.models import Program
from typing import List

association_table_apprentices = Table(
    "apprentices_groups",
    Base.metadata,
    Column('apprentice_id', ForeignKey("users.id"), primary_key=True),
    Column('group_id', ForeignKey("groups.id"), primary_key=True)
)

association_table_instructor = Table(
    "instructors_groups",
    Base.metadata,
    Column("instructor_id", ForeignKey("users.id"), primary_key=True),
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
)


class StatusGroup(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class Group(Base):
    __tablename__ = "groups"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    modality: Mapped[str] = mapped_column(String(60), nullable=False)
    start_date: Mapped[str] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[str] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(SqlALchemyEnum(StatusGroup), nullable=False, default=StatusGroup.ACTIVE)

    # Add program relationship
    program_id: Mapped[str] = mapped_column(ForeignKey("programs.id"))
    program: Mapped["Program"] = relationship(back_populates="groups")

    # Add apprentices relationship
    apprentices: Mapped[List["User"]] = relationship(secondary=association_table_apprentices, back_populates="group_apprentices")
    instructors: Mapped[List["User"]] = relationship(secondary=association_table_instructor, back_populates="group_instructors")