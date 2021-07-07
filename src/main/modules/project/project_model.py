from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Sequence

# import src.app as app
# db = app.db
from src.app import db


class Project(db.Model):
    __tablename__ = 'Projects'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(50), primary_key=True, index=True)
    descriptions = db.Column(db.String(75), index=True)
    
    user_id = db.Column(db.String(100), ForeignKey('Users.email'))
    user = relationship('User', backref='projects')

    def __repr__(self):
        return f"<Project: name: {self.full_name}, descriptions: {self.descriptions}>"

