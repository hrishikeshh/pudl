"""purchased storage mwh.

Revision ID: 273a78878b74
Revises: b5226cb31143
Create Date: 2023-09-22 12:46:04.273518

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '273a78878b74'
down_revision = 'b5226cb31143'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('denorm_purchased_power_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('purchased_storage_mwh', sa.Float(), nullable=True, comment='Number of megawatt hours purchased for energy storage during the period.'))
        batch_op.add_column(sa.Column('purchased_other_than_storage_mwh', sa.Float(), nullable=True, comment='Number of megawatt hours purchased for other than energy storage during the period.'))

    with op.batch_alter_table('purchased_power_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('purchased_storage_mwh', sa.Float(), nullable=True, comment='Number of megawatt hours purchased for energy storage during the period.'))
        batch_op.add_column(sa.Column('purchased_other_than_storage_mwh', sa.Float(), nullable=True, comment='Number of megawatt hours purchased for other than energy storage during the period.'))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchased_power_ferc1', schema=None) as batch_op:
        batch_op.drop_column('purchased_other_than_storage_mwh')
        batch_op.drop_column('purchased_storage_mwh')

    with op.batch_alter_table('denorm_purchased_power_ferc1', schema=None) as batch_op:
        batch_op.drop_column('purchased_other_than_storage_mwh')
        batch_op.drop_column('purchased_storage_mwh')

    # ### end Alembic commands ###
