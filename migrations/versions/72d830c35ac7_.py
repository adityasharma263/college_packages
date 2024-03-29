"""empty message

Revision ID: 72d830c35ac7
Revises: 13cc8ebc0c54
Create Date: 2019-07-28 14:30:48.993380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d830c35ac7'
down_revision = '13cc8ebc0c54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('college_selected_package', sa.Column('booking_date', sa.DateTime(), nullable=True))
    op.drop_constraint('college_selected_package_availability_id_fkey', 'college_selected_package', type_='foreignkey')
    op.drop_column('college_selected_package', 'availability_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('college_selected_package', sa.Column('availability_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('college_selected_package_availability_id_fkey', 'college_selected_package', 'availability', ['availability_id'], ['id'])
    op.drop_column('college_selected_package', 'booking_date')
    # ### end Alembic commands ###
