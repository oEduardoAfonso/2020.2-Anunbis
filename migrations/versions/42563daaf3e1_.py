"""empty message

Revision ID: 42563daaf3e1
Revises: ed3631c37ddd
Create Date: 2021-05-10 14:57:56.865511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42563daaf3e1'
down_revision = 'ed3631c37ddd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'course', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'course', type_='unique')
    # ### end Alembic commands ###
