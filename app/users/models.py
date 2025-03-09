import uuid
from datetime import datetime
from app.authorization.models import Role
from providers.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Enum as SqlALchemyEnum, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum
from typing import List
from app.groups.models import (
    association_table_apprentices,
    Group,
    association_table_instructor
)
from sqlalchemy.ext.hybrid import hybrid_property

class DocumentType(str, Enum):
    RC = "RC"
    TI = "TI"
    CC = "CC"
    TE = "TE"
    CE = "CE"
    NIT = "NIT"
    PP = "PP"
    PEP = "PEP"
    DIE = "DIE"
    NUIP = "NUIP"
    FOREIGN_NIT = "FOREIGN_NIT"

class StatusType(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100))
    document_type: Mapped[str] = mapped_column(SqlALchemyEnum(DocumentType), nullable=False)
    document: Mapped[str] = mapped_column(String(12), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    avatar: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(SqlALchemyEnum(StatusType), nullable=False, default=StatusType.ACTIVE)
    password: Mapped[str] = mapped_column(Text, nullable=True)

    # Add roles relationship.
    role_id: Mapped[str] = mapped_column(ForeignKey("roles.id"))
    role: Mapped["Role"] = relationship(back_populates="users")

    group_apprentices: Mapped[List["Group"]] = relationship(secondary=association_table_apprentices, back_populates="apprentices")
    group_instructors: Mapped[List["Group"]] = relationship(secondary=association_table_instructor, back_populates="instructors")

    @hybrid_property
    def groups(self):
        if self.role.name == "apprentice":
            return self.group_apprentices
        elif self.role.name == "instructor":
            return self.group_instructors
        else:
            return []