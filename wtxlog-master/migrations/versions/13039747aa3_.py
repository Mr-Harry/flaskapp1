"""empty message

Revision ID: 13039747aa3
Revises: 573c11d104ad
Create Date: 2014-12-05 11:02:12.375633

"""

# revision identifiers, used by Alembic.
revision = '13039747aa3'
down_revision = '573c11d104ad'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('rawvalue', sa.String(length=4096), nullable=False),
    sa.Column('formatter', sa.String(length=16), nullable=False),
    sa.Column('builtin', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('settings')
    ### end Alembic commands ###