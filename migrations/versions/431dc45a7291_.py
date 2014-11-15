"""empty message

Revision ID: 431dc45a7291
Revises: 4cd93da0e969
Create Date: 2014-11-15 22:31:01.253839

"""

# revision identifiers, used by Alembic.
revision = '431dc45a7291'
down_revision = '4cd93da0e969'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('logical_id', sa.String(length=256), nullable=True),
    sa.Column('start_time', sa.Float(), nullable=True),
    sa.Column('end_time', sa.Float(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('skipped', sa.Boolean(), nullable=True),
    sa.Column('num_errors', sa.Integer(), nullable=True),
    sa.Column('num_failures', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_logical_id'), 'test', ['logical_id'], unique=False)
    op.create_index(op.f('ix_test_name'), 'test', ['name'], unique=False)
    op.create_index(op.f('ix_test_session_id'), 'test', ['session_id'], unique=False)
    op.create_table('test_metadata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.Column('metadata_item', postgresql.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['test_id'], ['test.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_metadata_test_id'), 'test_metadata', ['test_id'], unique=False)
    op.add_column(u'session', sa.Column('logical_id', sa.String(length=256), nullable=True))
    op.add_column(u'session', sa.Column('product_name', sa.String(length=256), nullable=True))
    op.add_column(u'session', sa.Column('product_revision', sa.String(length=256), nullable=True))
    op.add_column(u'session', sa.Column('product_version', sa.String(length=256), nullable=True))
    op.add_column(u'session', sa.Column('user_name', sa.String(length=256), nullable=True))
    op.create_index(op.f('ix_session_logical_id'), 'session', ['logical_id'], unique=False)
    op.create_index(op.f('ix_session_product_name'), 'session', ['product_name'], unique=False)
    op.create_index(op.f('ix_session_product_revision'), 'session', ['product_revision'], unique=False)
    op.create_index(op.f('ix_session_product_version'), 'session', ['product_version'], unique=False)
    op.create_index(op.f('ix_session_user_name'), 'session', ['user_name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_session_user_name'), table_name='session')
    op.drop_index(op.f('ix_session_product_version'), table_name='session')
    op.drop_index(op.f('ix_session_product_revision'), table_name='session')
    op.drop_index(op.f('ix_session_product_name'), table_name='session')
    op.drop_index(op.f('ix_session_logical_id'), table_name='session')
    op.drop_column(u'session', 'user_name')
    op.drop_column(u'session', 'product_version')
    op.drop_column(u'session', 'product_revision')
    op.drop_column(u'session', 'product_name')
    op.drop_column(u'session', 'logical_id')
    op.drop_index(op.f('ix_test_metadata_test_id'), table_name='test_metadata')
    op.drop_table('test_metadata')
    op.drop_index(op.f('ix_test_session_id'), table_name='test')
    op.drop_index(op.f('ix_test_name'), table_name='test')
    op.drop_index(op.f('ix_test_logical_id'), table_name='test')
    op.drop_table('test')
    ### end Alembic commands ###
