"""empty message

Revision ID: 1b51b1bd9939
Revises: 
Create Date: 2019-12-28 22:33:17.572513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b51b1bd9939'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('circle',
    sa.Column('circle_id', sa.Integer(), nullable=False),
    sa.Column('circle_name', sa.String(length=20), nullable=True),
    sa.Column('people_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('circle_id'),
    sa.UniqueConstraint('circle_name')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('nick_name', sa.String(length=50), nullable=True),
    sa.Column('profile', sa.String(length=100), nullable=True),
    sa.Column('intro', sa.Text(), nullable=True),
    sa.Column('circle1', sa.Integer(), nullable=True),
    sa.Column('circle2', sa.Integer(), nullable=True),
    sa.Column('circle3', sa.Integer(), nullable=True),
    sa.Column('circle4', sa.Integer(), nullable=True),
    sa.Column('circle5', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('circle_id', sa.Integer(), nullable=True),
    sa.Column('postTime', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('content', sa.String(length=10000), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('favorites', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['circle_id'], ['circle.circle_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('block',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('post_id', 'user_id')
    )
    op.create_table('comment',
    sa.Column('Comment_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment_to', sa.Integer(), nullable=True),
    sa.Column('commentTime', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('content', sa.String(length=10000), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_to'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('Comment_id')
    )
    op.create_table('favorite',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('favoriteTime', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('post_id', 'user_id')
    )
    op.create_table('like',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('like_to', sa.Integer(), nullable=True),
    sa.Column('likeTime', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['like_to'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('post_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like')
    op.drop_table('favorite')
    op.drop_table('comment')
    op.drop_table('block')
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('circle')
    # ### end Alembic commands ###
