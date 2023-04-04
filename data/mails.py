import datetime
import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Mail(SqlAlchemyBase, UserMixin):
    __tablename__ = 'mails'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    send_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())