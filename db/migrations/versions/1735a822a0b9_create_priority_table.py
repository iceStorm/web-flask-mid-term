"""create Priority table

Revision ID: 1735a822a0b9
Revises: 
Create Date: 2021-07-09 07:34:13.300195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1735a822a0b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Priorities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Users',
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('avatar_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Users_email'), ['email'], unique=False)
        batch_op.create_index(batch_op.f('ix_Users_full_name'), ['full_name'], unique=False)

    op.create_table('Projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('descriptions', sa.String(length=75), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('status_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['status_id'], ['Statuses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['Users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Projects', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Projects_descriptions'), ['descriptions'], unique=False)
        batch_op.create_index(batch_op.f('ix_Projects_name'), ['name'], unique=True)

    op.create_table('Tasks',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('trashed', sa.Boolean(), nullable=False),
    sa.Column('priority_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.String(length=100), nullable=False),
    sa.Column('status_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['priority_id'], ['Priorities.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['Projects.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['Statuses.id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Tasks')
    with op.batch_alter_table('Projects', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Projects_name'))
        batch_op.drop_index(batch_op.f('ix_Projects_descriptions'))

    op.drop_table('Projects')
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Users_full_name'))
        batch_op.drop_index(batch_op.f('ix_Users_email'))

    op.drop_table('Users')
    op.drop_table('Statuses')
    op.drop_table('Priorities')
    # ### end Alembic commands ###