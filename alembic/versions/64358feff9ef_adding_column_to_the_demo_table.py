"""Adding column to the demo table

Revision ID: 64358feff9ef
Revises: 689d0dce9c3c
Create Date: 2022-06-01 16:18:01.930108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64358feff9ef'
down_revision = '689d0dce9c3c'
branch_labels = None
depends_on = None


def upgrade():
        op.add_column('demo', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')))


def downgrade():
        op.drop_column('demo', 'created_at')
