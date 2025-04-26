from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'aacdef123456'
down_revision = 'abcdef123456'
branch_labels = None
depends_on = None


def upgrade():
    categories_table = sa.table(
        'categories',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String())
    )
    op.bulk_insert(
        categories_table,
        [
            {'id': 4, 'name': 'Sweets'}
        ]
    )


def downgrade():
    op.execute(
        "DELETE FROM categories"
        "WHERE id = 4"
    )
