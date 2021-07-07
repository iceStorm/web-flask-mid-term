from sqlalchemy import Sequence

# import src.app as app
# db = app.db
from src.app import db


class Priority(db.Model):
  __tablename__ = "Priorities"
  __table_args__ = {'extend_existing': True}

  id = db.Column(db.Integer, Sequence('priority_id_seq'), primary_key=True)
  name = db.Column(db.String(20), nullable=False, unique=True)


  def __repr__(self) -> str:
    return f'<Priority: user: {self.id} | description: {self.name}>'
