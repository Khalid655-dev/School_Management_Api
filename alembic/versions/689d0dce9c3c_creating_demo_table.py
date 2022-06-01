"""Creating Demo Table

Revision ID: 689d0dce9c3c
Revises: 
Create Date: 2022-06-01 16:07:35.038835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '689d0dce9c3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'demo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('demo')

