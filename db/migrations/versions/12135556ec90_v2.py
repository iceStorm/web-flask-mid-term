"""v2

Revision ID: 12135556ec90
Revises: 03fb94aede7b
Create Date: 2021-05-28 20:42:30.738317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12135556ec90'
down_revision = '03fb94aede7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###