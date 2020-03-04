import sqlalchemy as sa
import datetime
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id_ = sa.Column(sa.Integer,
                    autoincrement=True,
                    primary_key=True,
                    name='id')
    team_leader = sa.Column(sa.Integer,
                            sa.ForeignKey('users.id'))
    job = sa.Column(sa.String, nullable=True)
    work_size = sa.Column(sa.Integer, nullable=True)
    collaborators = sa.Column(sa.String, nullable=True)
    start_date = sa.Column(sa.DateTime,
                           nullable=True,
                           default=datetime.datetime.now)
    end_date = sa.Column(sa.DateTime, nullable=True)
    is_finished = sa.Column(sa.Boolean, nullable=True)

    def __repr__(self):
        return f'<Job> {self.job}'
