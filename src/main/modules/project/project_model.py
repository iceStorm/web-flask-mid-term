from src.app import db
from sqlalchemy import Sequence


class Project(db.Model):
    __tablename__ = 'Projects'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(50), primary_key=True, index=True)
    descriptions = db.Column(db.String(75), index=True)

    def __repr__(self):
        return f"<Project: name: {self.full_name}, descriptions: {self.descriptions}>"

