"""empty message

Revision ID: e07ba062655d
Revises: 6f69344fd2d1
Create Date: 2023-10-07 13:01:02.542133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e07ba062655d'
down_revision = '6f69344fd2d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('room', sa.Column('members', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('room', 'members')
    # ### end Alembic commands ###
