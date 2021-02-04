"""empty message

Revision ID: 6017dab0ffd9
Revises: 
Create Date: 2019-07-12 17:06:44.486199

"""
# 3rd party
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "6017dab0ffd9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "torrents",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("path", sa.String(), nullable=True),
        sa.Column(
            "status",
            sa.Enum(
                "COMPLETED",
                "ENQUEUED",
                "FAILED",
                "IGNORED",
                "NEEDS_INPUT",
                "PROCESSING",
                name="status",
            ),
            nullable=True,
        ),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "lines",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("index", sa.Integer(), nullable=True),
        sa.Column("data", sa.String(), nullable=True),
        sa.Column("torrent_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["torrent_id"], ["torrents.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("lines")
    op.drop_table("torrents")
    # ### end Alembic commands ###