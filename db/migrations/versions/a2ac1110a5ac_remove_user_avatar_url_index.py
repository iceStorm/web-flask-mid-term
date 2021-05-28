"""remove User avatar_url Index

Revision ID: a2ac1110a5ac
Revises: b20e89d9f14b
Create Date: 2021-05-28 16:52:01.620980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2ac1110a5ac'
down_revision = 'b20e89d9f14b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_index('ix_Users_avatar_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.create_index('ix_Users_avatar_url', ['avatar_url'], unique=False)

    # ### end Alembic commands ###
