from sqlalchemy import Sequence

from src.app import db


class Status(db.Model):
    __tablename__ = 'Statuses'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, Sequence(name='status_id_seq'), primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"<Status id: {self.id} name: {self.name}>"
