"""Index start/end times

Revision ID: c9b38de7bf68
Revises: 323f8d77567b
Create Date: 2016-11-17 15:53:49.243454

"""

# revision identifiers, used by Alembic.
revision = 'c9b38de7bf68'
down_revision = '323f8d77567b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_test_end_time'), 'test', ['end_time'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_test_end_time'), table_name='test')
    ### end Alembic commands ###
