"""empty message

Revision ID: 101774dd0b49
Revises: 41b47521ca32
Create Date: 2020-08-28 20:24:45.629301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '101774dd0b49'
down_revision = '41b47521ca32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('slug', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'recipes', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='unique')
    op.drop_column('recipes', 'slug')
    # ### end Alembic commands ###
