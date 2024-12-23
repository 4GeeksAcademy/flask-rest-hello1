"""empty message

Revision ID: 25edd375edcb
Revises: 3d49136e4d7e
Create Date: 2023-1-14 15:18:09.385877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25edd375edcb'
down_revision = '3d49136e4d7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('persom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['persom_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('favorite_planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('planet_size', sa.String(length=120), nullable=False))

    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_size', sa.String(length=120), nullable=True))
        batch_op.alter_column('planet_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.create_unique_constraint(None, ['planet_size'])
        batch_op.drop_column('planet_id')
        batch_op.drop_column('is_active')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('planet_id', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('planet_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.drop_column('planet_size')

    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))

    with op.batch_alter_table('favorite_planet', schema=None) as batch_op:
        batch_op.drop_column('planet_size')
        batch_op.drop_column('planet_name')

    op.drop_table('favorite_person')
    # ### end Alembic commands ###
