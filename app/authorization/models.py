import uuid
from enum import Enum
from datetime import datetime
from providers.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import (
    String,
    Table,
    DateTime,
    Enum as SqlALchemyEnum,
    Text,
    Column,
    ForeignKey
)

class StatusType(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

association_table = Table(
    "permissions_roles",
    Base.metadata,
    Column('role_id', ForeignKey("roles.id"), primary_key=True),
    Column('permission_id', ForeignKey("permissions.id"), primary_key=True)
)

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    status: Mapped[str] = mapped_column(SqlALchemyEnum(StatusType), nullable=False, default=StatusType.ACTIVE)

    # Add relationship Permissions
    permissions: Mapped[List["Permission"]] = relationship(secondary=association_table, back_populates="roles")
    
    # Add relationship User
    users: Mapped[List["User"]] = relationship(back_populates="role")

class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    status: Mapped[str] = mapped_column(SqlALchemyEnum(StatusType), nullable=False, default=StatusType.ACTIVE)

    # Add relationship Roles
    roles: Mapped[List[Role]] = relationship(secondary=association_table, back_populates="permissions")