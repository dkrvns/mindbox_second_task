from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'abcdef123456'
down_revision = 'c470c88a92fa'
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
            {'id': 1, 'name': 'Electronics'},
            {'id': 2, 'name': 'Clothing'},
            {'id': 3, 'name': 'Books'}
        ]
    )

    products_table = sa.table(
        'products',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String())
    )
    op.bulk_insert(
        products_table,
        [
            {'id': 1, 'name': 'Laptop'},
            {'id': 2, 'name': 'T-shirt'},
            {'id': 3, 'name': 'Novel'},
            {'id': 4, 'name': 'Headphones'},
            {'id': 5, 'name': 'Jeans'},
            {'id': 6, 'name': 'Smartphone'}
        ]
    )

    product_category_table = sa.table(
        'product_category',
        sa.Column('product_id', sa.Integer()),
        sa.Column('category_id', sa.Integer())
    )
    op.bulk_insert(
        product_category_table,
        [
            {'product_id': 1, 'category_id': 1},
            {'product_id': 2, 'category_id': 2},
            {'product_id': 3, 'category_id': 3},
            {'product_id': 4, 'category_id': 1},
            {'product_id': 5, 'category_id': 2}
        ]
    )


def downgrade():
    op.execute("DELETE FROM product_category")
    op.execute("DELETE FROM products")
    op.execute("DELETE FROM categories")
