"""change Project model pk to name

Revision ID: 8655de4746bd
Revises: a2ac1110a5ac
Create Date: 2021-05-28 17:12:29.468903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8655de4746bd'
down_revision = 'a2ac1110a5ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Projects', schema=None) as batch_op:
        batch_op.drop_index('ix_Projects_id')
        batch_op.drop_index('ix_Projects_name')

    op.drop_table('Projects')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Projects',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('descriptions', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Projects', schema=None) as batch_op:
        batch_op.create_index('ix_Projects_name', ['name'], unique=False)
        batch_op.create_index('ix_Projects_id', ['id'], unique=False)

    # ### end Alembic commands ###
