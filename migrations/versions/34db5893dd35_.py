"""empty message

Revision ID: 34db5893dd35
Revises: bc128bb93834
Create Date: 2024-03-27 11:26:05.324980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34db5893dd35'
down_revision = 'bc128bb93834'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project_members', schema=None) as batch_op:
        batch_op.drop_constraint('project_members_project_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'project', ['project_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project_members', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('project_members_project_id_fkey', 'project', ['project_id'], ['id'])

    # ### end Alembic commands ###
