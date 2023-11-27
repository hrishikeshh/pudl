"""add utility type to liabilities side

Revision ID: 7febe79b8760
Revises: ad3e7ecdcfc3
Create Date: 2023-09-28 11:10:01.521413

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7febe79b8760"
down_revision = "ad3e7ecdcfc3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(
        "balance_sheet_liabilities_ferc1", schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "utility_type",
                sa.Text(),
                nullable=True,
                comment="Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.",
            )
        )

    with op.batch_alter_table(
        "denorm_balance_sheet_liabilities_ferc1", schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "utility_type",
                sa.Text(),
                nullable=True,
                comment="Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.",
            )
        )

    with op.batch_alter_table(
        "denorm_retained_earnings_ferc1", schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "utility_type",
                sa.Text(),
                nullable=True,
                comment="Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.",
            )
        )

    with op.batch_alter_table("retained_earnings_ferc1", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "utility_type",
                sa.Text(),
                nullable=True,
                comment="Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.",
            )
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("retained_earnings_ferc1", schema=None) as batch_op:
        batch_op.drop_column("utility_type")

    with op.batch_alter_table(
        "denorm_retained_earnings_ferc1", schema=None
    ) as batch_op:
        batch_op.drop_column("utility_type")

    with op.batch_alter_table(
        "denorm_balance_sheet_liabilities_ferc1", schema=None
    ) as batch_op:
        batch_op.drop_column("utility_type")

    with op.batch_alter_table(
        "balance_sheet_liabilities_ferc1", schema=None
    ) as batch_op:
        batch_op.drop_column("utility_type")

    # ### end Alembic commands ###
