"""empty message

Revision ID: e85ce4de86e4
Revises: 1c82b0b9a657
Create Date: 2021-05-16 02:20:18.847843

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e85ce4de86e4'
down_revision = '1c82b0b9a657'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('professor', 'email',
               existing_type=sa.String(collation='utf8_unicode_ci', length=255),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('student', 'password',
               existing_type=sa.String(collation='utf8_unicode_ci', length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('reg_student', 'student', ['reg_student'], unique=False)
    op.alter_column('student', 'password',
               existing_type=mysql.VARCHAR(collation='utf8_unicode_ci', length=255),
               nullable=False)
    op.alter_column('professor', 'email',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(collation='utf8_unicode_ci', length=255),
               existing_nullable=True)
    # ### end Alembic commands ###
