import sqlalchemy
import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id_ = sqlalchemy.Column(sqlalchemy.Integer,
                            primary_key=True,
                            autoincrement=True,
                            name='id')
    surname = sqlalchemy.Column(sqlalchemy.String,
                                nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String,
                             nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer,
                            nullable=True)
    position = sqlalchemy.Column(sqlalchemy.Integer,
                                 nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String,
                                   nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String,
                                nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              unique=True,
                              index=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)

    def __repr__(self):
        return f'<Colonist> {self.id_} {self.surname} {self.name}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
