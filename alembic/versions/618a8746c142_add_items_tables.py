"""Add items tables

Revision ID: 618a8746c142
Revises: 531b2a49c52b
Create Date: 2020-11-23 17:52:05.149409

"""
from datetime import datetime

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "618a8746c142"
down_revision = "531b2a49c52b"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "analysis",
        sa.Column("id", sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.BIGINT(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("created_at", sa.DateTime(), default=datetime.now(), nullable=False),
        sa.Column("category_id", sa.BIGINT(), nullable=False),
        sa.Column("comment", sa.String(), nullable=True)
    )

    op.create_index(op.f("ix_analysis_user_id"), "analysis", ["user_id"])
    op.create_index(op.f("ix_analysis_category_id"), "analysis", ["category_id"])

    op.create_table(
        "image_blob",
        sa.Column("id", sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.BIGINT(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("filename", sa.String(), nullable=False),
        sa.Column("content_type", sa.String(), nullable=False),
        sa.Column("byte_size", sa.BIGINT(), nullable=False),
        sa.Column("check_sum", sa.String(), nullable=False),
        sa.Column(
            "analysis_id", sa.BIGINT(), sa.ForeignKey("analysis.id"), default=None
        ),
        sa.Column("position", sa.BIGINT(), nullable=False),
        sa.Column("created_at", sa.DateTime(), default=datetime.now(), nullable=False),
    )

    op.create_index(op.f("ix_image_analysis_id"), "image_blob", ["analysis_id"])
    op.create_index(op.f("ix_image_user_id"), "image_blob", ["user_id"])


def downgrade():
    op.drop_index(op.f("ix_analysis_user_id"), table_name="analysis")
    op.drop_table("analysis")

    op.drop_index(op.f("ix_image"), table_name="image_blob")
    op.drop_table("image_blob")
