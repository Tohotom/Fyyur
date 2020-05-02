"""empty message

Revision ID: 971c0579fb84
Revises: 54d450ac3d88
Create Date: 2020-05-02 11:42:08.064130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '971c0579fb84'
down_revision = '54d450ac3d88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('City',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Artist', sa.Column('city_id', sa.Integer(), nullable=False))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.create_foreign_key(None, 'Artist', 'City', ['city_id'], ['id'])
    op.drop_column('Artist', 'state')
    op.drop_column('Artist', 'city')
    op.add_column('Venue', sa.Column('city_id', sa.Integer(), nullable=False))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    op.create_foreign_key(None, 'Venue', 'City', ['city_id'], ['id'])
    op.drop_column('Venue', 'state')
    op.drop_column('Venue', 'city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'city_id')
    op.add_column('Artist', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Artist', type_='foreignkey')
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'city_id')
    op.drop_table('Genre')
    op.drop_table('City')
    # ### end Alembic commands ###
