from sqlalchemy import Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

# import src.app as app
# db = app.db
from src.app import db


class Task(db.Model):
    __tablename__ = "Tasks"
    __table_args__ = {'extend_existing': True}

    task_id = db.Column(db.Integer, Sequence('task_id_seq'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    trashed = db.Column(db.Boolean, nullable=False)

    user_id = db.Column(db.String(100), ForeignKey('Users.email'), nullable=False)
    user = relationship('User', backref=db.backref('tasks', lazy='joined'))

    priority_id = db.Column(db.Integer, ForeignKey('Priorities.id'), nullable=False)
    priority = relationship('Priority', backref=db.backref('tasks', lazy='joined'))


    def __repr__(self) -> str:
        return f'<Task: user: {self.user_id} | description: {self.description}>'


    def get_priority_class(self):
        """
        @return: the css class (background color) corresponding to the priority level.
        """
        if self.priority.name == 'Lowest':
            return 'bg-green-200'
        elif self.priority.name == 'Low':
            return 'bg-blue-200'
        elif self.priority.name == 'Medium':
            return 'bg-yellow-200'
        else:
            return 'bg-red-200'
