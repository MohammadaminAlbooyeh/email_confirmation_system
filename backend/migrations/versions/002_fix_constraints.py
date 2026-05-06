"""Fix nullable constraints and add CASCADE on foreign key.

Revision ID: 002_fix_constraints
Revises: 001_initial_schema
Create Date: 2026-05-06 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_fix_constraints'
down_revision = '001_initial_schema'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add NOT NULL constraints to critical columns
    op.alter_column('users', 'email',
               existing_type=sa.String(),
               nullable=False)
    op.alter_column('users', 'password_hash',
               existing_type=sa.String(),
               nullable=False)
    op.alter_column('confirmation_tokens', 'user_id',
               existing_type=sa.Integer(),
               nullable=False)
    op.alter_column('confirmation_tokens', 'token',
               existing_type=sa.String(),
               nullable=False)

    # Drop and recreate foreign key with CASCADE
    op.drop_constraint('confirmation_tokens_user_id_fkey', 'confirmation_tokens', type_='foreignkey')
    op.create_foreign_key(
        'confirmation_tokens_user_id_fkey',
        'confirmation_tokens', 'users',
        ['user_id'], ['id'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    # Revert foreign key
    op.drop_constraint('confirmation_tokens_user_id_fkey', 'confirmation_tokens', type_='foreignkey')
    op.create_foreign_key(
        'confirmation_tokens_user_id_fkey',
        'confirmation_tokens', 'users',
        ['user_id'], ['id']
    )

    # Revert nullable constraints
    op.alter_column('users', 'email',
               existing_type=sa.String(),
               nullable=True)
    op.alter_column('users', 'password_hash',
               existing_type=sa.String(),
               nullable=True)
    op.alter_column('confirmation_tokens', 'user_id',
               existing_type=sa.Integer(),
               nullable=True)
    op.alter_column('confirmation_tokens', 'token',
               existing_type=sa.String(),
               nullable=True)
