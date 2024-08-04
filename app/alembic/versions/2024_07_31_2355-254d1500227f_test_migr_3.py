"""test_migr_3

Revision ID: 254d1500227f
Revises: 
Create Date: 2024-07-31 23:55:53.030037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '254d1500227f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('english', sa.String(), nullable=True),
    sa.Column('russian', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('difficulty', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cards'))
    )
    op.create_index(op.f('ix_cards_english'), 'cards', ['english'], unique=False)
    op.create_index(op.f('ix_cards_id'), 'cards', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('learning_progress',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.Column('right_answers', sa.Integer(), nullable=False),
    sa.Column('wrong_answers', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['cards.id'], name=op.f('fk_learning_progress_card_id_cards')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_learning_progress_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'card_id', name='pk_user_card')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('learning_progress')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_cards_id'), table_name='cards')
    op.drop_index(op.f('ix_cards_english'), table_name='cards')
    op.drop_table('cards')
    # ### end Alembic commands ###