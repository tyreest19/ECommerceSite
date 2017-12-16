"""empty message

Revision ID: f1cc0af935cd
Revises: 
Create Date: 2017-12-15 17:56:09.978002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1cc0af935cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SignUpTable',
    sa.Column('twitterHandle', sa.VARCHAR(length=100), nullable=True),
    sa.Column('instagramHandle', sa.VARCHAR(length=100), nullable=True),
    sa.Column('signupID', sa.Integer(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=True),
    sa.Column('pintrestHandle', sa.VARCHAR(length=100), nullable=True),
    sa.Column('tumblrHandle', sa.VARCHAR(length=100), nullable=True),
    sa.Column('youtubeHandle', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('signupID')
    )
    op.create_table('User',
    sa.Column('fname', sa.VARCHAR(length=100), nullable=True),
    sa.Column('lname', sa.VARCHAR(length=100), nullable=True),
    sa.Column('username', sa.VARCHAR(length=100), nullable=True),
    sa.Column('address', sa.VARCHAR(length=100), nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.Column('birthdate', sa.DATE(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('userID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User')
    op.drop_table('SignUpTable')
    # ### end Alembic commands ###
