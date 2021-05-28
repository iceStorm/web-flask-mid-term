"""v2

Revision ID: 03fb94aede7b
Revises: 5ab39c9e4d5c
Create Date: 2021-05-28 20:41:58.714601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03fb94aede7b'
down_revision = '5ab39c9e4d5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.alter_column('full_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.drop_index('ix_Users_avatar_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.create_index('ix_Users_avatar_url', ['avatar_url'], unique=False)
        batch_op.alter_column('full_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###
