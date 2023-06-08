"""Add reviews table

Revision ID: b92790a03a28
Revises: 6c71f71be7e5
Create Date: 2023-06-08 09:54:03.905234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b92790a03a28'
down_revision = '6c71f71be7e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('hotel_id', sa.Integer(), nullable=False),
        sa.Column('customer_id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('reviews')
