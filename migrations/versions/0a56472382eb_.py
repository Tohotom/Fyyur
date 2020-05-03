"""empty message

Revision ID: 0a56472382eb
Revises: eadd3626a67f
Create Date: 2020-05-02 16:22:54.736454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a56472382eb'
down_revision = 'eadd3626a67f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('num_past_shows', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'num_past_shows')
    # ### end Alembic commands ###
