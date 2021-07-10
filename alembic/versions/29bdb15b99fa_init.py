"""init

Revision ID: 29bdb15b99fa
Revises: 
Create Date: 2021-07-10 10:37:58.799337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29bdb15b99fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_providers_id', table_name='providers')
    op.drop_table('providers')
    op.drop_index('ix_products_id', table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('qty', sa.INTEGER(), nullable=False),
    sa.Column('provider_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['provider_id'], ['providers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_products_id', 'products', ['id'], unique=False)
    op.create_table('providers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_providers_id', 'providers', ['id'], unique=False)
    # ### end Alembic commands ###