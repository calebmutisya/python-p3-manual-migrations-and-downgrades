"""Renaming students to scholars

Revision ID: 34f7156d4f39
Revises: 791279dd0760
Create Date: 2023-12-06 15:04:01.950599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34f7156d4f39'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
