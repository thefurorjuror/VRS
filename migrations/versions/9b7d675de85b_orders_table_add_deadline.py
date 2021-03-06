"""orders table add deadline

Revision ID: 9b7d675de85b
Revises: b7afa54d18b0
Create Date: 2022-03-28 10:49:58.628956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b7d675de85b'
down_revision = 'b7afa54d18b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('deadline', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_order_deadline'), 'order', ['deadline'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_deadline'), table_name='order')
    op.drop_column('order', 'deadline')
    # ### end Alembic commands ###
