"""create program and group model

Revision ID: adf13cc7997e
Revises: 9273135e763d
Create Date: 2025-02-23 11:02:25.077270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adf13cc7997e'
down_revision: Union[str, None] = '9273135e763d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('programs',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('type', sa.Enum('TECHNICIAN', 'TECHNOLOGIST', 'UNDERGRADUATE', 'POSTGRADUATE', name='typeprogram'), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('certificate', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Enum('ACTIVE', 'INACTIVE', name='statusprogram'), nullable=False),
    sa.Column('timing_system', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modality', sa.String(length=60), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('ACTIVE', 'INACTIVE', name='statusgroup'), nullable=False),
    sa.Column('program_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groups')
    op.drop_table('programs')
    # ### end Alembic commands ###
