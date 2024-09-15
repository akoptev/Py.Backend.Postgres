"""Seed data

Revision ID: a9a689b9d9d3
Revises: 7d35e9457156
Create Date: 2024-09-15 11:29:46.424231

"""

from migrations.seeding import delete_records, seed_questions


# revision identifiers, used by Alembic.
revision = "a9a689b9d9d3"
down_revision = "7d35e9457156"
branch_labels = None
depends_on = None


def upgrade() -> None:
    delete_records()
    seed_questions()


def downgrade() -> None:
    delete_records()
