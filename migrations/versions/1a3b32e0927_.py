"""empty message

Revision ID: 1a3b32e0927
Revises: f568e40f06
Create Date: 2015-07-08 22:48:01.467963

"""

# revision identifiers, used by Alembic.
revision = '1a3b32e0927'
down_revision = 'f568e40f06'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('error', 'exception', new_column_name='message')
    op.create_index(op.f('ix_error_message'), 'error', ['message'], unique=False)
    op.drop_index('ix_error_exception', table_name='error')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('error', 'message', new_column_name='exception')
    op.create_index('ix_error_exception', 'error', ['exception'], unique=False)
    op.drop_index(op.f('ix_error_message'), table_name='error')
    ### end Alembic commands ###