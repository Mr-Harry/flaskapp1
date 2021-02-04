"""empty message

Revision ID: 3cd10cfce8c3
Revises: 5e549314e1e2
Create Date: 2019-06-27 10:40:12.606337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd10cfce8c3'
down_revision = '5e549314e1e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authorization_code', sa.Column('redirect_uri', sa.String(length=1024), nullable=True))
    op.add_column('authorization_code', sa.Column('scope', sa.String(length=128), nullable=True))
    op.add_column('oauth_token', sa.Column('redirect_uri', sa.String(length=1024), nullable=True))
    op.add_column('oauth_token', sa.Column('scope', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('oauth_token', 'scope')
    op.drop_column('oauth_token', 'redirect_uri')
    op.drop_column('authorization_code', 'scope')
    op.drop_column('authorization_code', 'redirect_uri')
    # ### end Alembic commands ###