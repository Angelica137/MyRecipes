"""empty message

Revision ID: 6b79a66e6c97
Revises: 
Create Date: 2020-08-03 10:32:20.235356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b79a66e6c97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'recipe', ['recipe_id'])
    op.create_unique_constraint(None, 'user', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'recipe', type_='unique')
    # ### end Alembic commands ###