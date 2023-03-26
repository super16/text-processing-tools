from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR


revision = "a15a2b56c651"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "corpora",
        Column(
            "id",
            INTEGER,
            autoincrement=True,
            index=True,
            primary_key=True,
            unique=True,
        ),
        Column(
            "title",
            VARCHAR(64),
            nullable=False,
            unique=True,
        ),
    )


def downgrade() -> None:
    op.drop_table("corpora")
