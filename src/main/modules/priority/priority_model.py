from sqlalchemy import Sequence


# from src.app import db
import src.app as app
db = app.db


class Priority(db.Model):
    __tablename__ = "Priorities"
    __table_args__ = {'extend_existing': True}

    # no need to put Sequence('priority_id_seq') below
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'<Priority: user: {self.id} | description: {self.name}>'
