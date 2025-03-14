"""add apprentinces and instructor relationship

Revision ID: 983014228154
Revises: 4ffe738ee0b7
Create Date: 2025-02-23 17:30:29.835774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '983014228154'
down_revision: Union[str, None] = '4ffe738ee0b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apprentices_groups',
    sa.Column('apprentice_id', sa.UUID(), nullable=False),
    sa.Column('group_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['apprentice_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('apprentice_id', 'group_id')
    )
    op.create_table('instructors_groups',
    sa.Column('instructor_id', sa.UUID(), nullable=False),
    sa.Column('group_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['instructor_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('instructor_id', 'group_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instructors_groups')
    op.drop_table('apprentices_groups')
    # ### end Alembic commands ###
