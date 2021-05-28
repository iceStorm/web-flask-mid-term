"""create table users -v1

Revision ID: 4ae6a6a77a1d
Revises: 
Create Date: 2021-05-28 16:00:03.681099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae6a6a77a1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=True),
    sa.Column('avatar_url', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Users_avatar_url'), ['avatar_url'], unique=False)
        batch_op.create_index(batch_op.f('ix_Users_email'), ['email'], unique=False)
        batch_op.create_index(batch_op.f('ix_Users_full_name'), ['full_name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Users_full_name'))
        batch_op.drop_index(batch_op.f('ix_Users_email'))
        batch_op.drop_index(batch_op.f('ix_Users_avatar_url'))

    op.drop_table('Users')
    # ### end Alembic commands ###
