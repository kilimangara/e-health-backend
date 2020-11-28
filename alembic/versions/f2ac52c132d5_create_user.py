"""create user

Revision ID: f2ac52c132d5
Revises:
Create Date: 2020-08-02 19:59:08.748737

"""
from datetime import datetime

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "f2ac52c132d5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column("phone", sa.String(), nullable=True, unique=True),
        sa.Column("status", sa.String(), nullable=True, default="created"),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("blood_type", sa.String(), nullable=True),
        sa.Column("birth_date", sa.Date(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.Column("height", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), default=datetime.now()),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(op.f("ix_phone"), "users", ["phone"], unique=True)
    op.create_index(op.f("ix_user_id"), "users", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    op.drop_index(op.f("ix_phone"), table_name="users")
    op.drop_index(op.f("ix_user_id"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###
