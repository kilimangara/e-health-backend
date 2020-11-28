"""Add items tables

Revision ID: 618a8746c142
Revises: 531b2a49c52b
Create Date: 2020-11-23 17:52:05.149409

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '618a8746c142'
down_revision = '531b2a49c52b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "analysis",
        sa.Column("id", sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.BIGINT(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column("created_at", sa.DateTime(), default=datetime.now()),
        sa.Column("category_id", sa.BIGINT()),
    )

    op.create_index(op.f("ix_analysis_user_id"), "analysis", ["user_id"])

    op.create_table(
        "imageBlob",
        sa.Column("id", sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column("filename", sa.String(), nullable=False),
        sa.Column("content_type", sa.String(), nullable=False),
        sa.Column("byte_size", sa.BIGINT(), nullable=False),
        sa.Column("check_sum", sa.String(), nullable=False),
        sa.Column("analysis_id", sa.BIGINT(), sa.ForeignKey('analysis.id'), default=None),
        sa.Column("position", sa.BIGINT(), nullable=False),
        sa.Column("created_at", sa.DateTime(), default=datetime.now())
    )

    op.create_index(op.f("ix_image"), "imageBlob", ["analysis_id"])


def downgrade():
    op.drop_index(op.f("ix_analysis_user_id"), table_name="analysis")
    op.drop_table("analysis")

    op.drop_index(op.f("ix_image"), table_name="imageBlob")
    op.drop_table("imageBlob")