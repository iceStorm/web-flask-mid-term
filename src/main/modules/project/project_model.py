from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Sequence


from src.app import db


class Project(db.Model):
    __tablename__ = 'Projects'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, Sequence(name='project_id_seq'), primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    descriptions = db.Column(db.String(75), index=True)
    deadline = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.String(100), ForeignKey('Users.email'), nullable=False)
    user = relationship('User', backref='projects')

    # status_id == 4 == not started
    status_id = db.Column(db.Integer, ForeignKey('Statuses.id'), nullable=False, default=4)
    status = relationship('Status', backref='projects')

    def __repr__(self):
        return f"<Project: name: {self.name}, descriptions: {self.descriptions}>"

