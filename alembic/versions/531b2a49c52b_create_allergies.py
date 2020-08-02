"""create allergies

Revision ID: 531b2a49c52b
Revises: f2ac52c132d5
Create Date: 2020-08-02 19:59:21.093667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '531b2a49c52b'
down_revision = 'f2ac52c132d5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "allergies",
        sa.Column("id", sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.BIGINT(), nullable=False),
        sa.Column("allergen", sa.String(), nullable=False),
        sa.Column("reaction", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user_data.id"], ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_allergie_user_id"), "allergies", ["user_id"])


def downgrade():
    op.drop_index(op.f("ix_allergie_user_id"), table_name="allergies")
    op.drop_table("allergies")
