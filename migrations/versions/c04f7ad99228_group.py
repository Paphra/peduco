"""group

Revision ID: c04f7ad99228
Revises: 2492b0572a3b
Create Date: 2019-04-06 11:38:27.556203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c04f7ad99228'
down_revision = '2492b0572a3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_code', sa.String(length=10), nullable=True),
    sa.Column('course_name', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_course_code'), 'group', ['course_code'], unique=False)
    op.create_index(op.f('ix_group_course_name'), 'group', ['course_name'], unique=False)
    op.create_index(op.f('ix_group_name'), 'group', ['name'], unique=False)
    op.create_table('members',
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('members')
    op.drop_index(op.f('ix_group_name'), table_name='group')
    op.drop_index(op.f('ix_group_course_name'), table_name='group')
    op.drop_index(op.f('ix_group_course_code'), table_name='group')
    op.drop_table('group')
    # ### end Alembic commands ###