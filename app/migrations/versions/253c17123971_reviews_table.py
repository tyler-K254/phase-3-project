"""Reviews table

Revision ID: 253c17123971
Revises: 1c1451d87d9f
Create Date: 2023-06-07 23:05:50.880105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '253c17123971'
down_revision = '1c1451d87d9f'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('restaurant_id', sa.Integer(), nullable=False),
        sa.Column('customer_id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('reviews')
