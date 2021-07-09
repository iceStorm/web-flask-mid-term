from sqlalchemy import Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


from src.app import db

class Task(db.Model):
    __tablename__ = "Tasks"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, Sequence('task_id_seq'), primary_key=True)
    descriptions = db.Column(db.String(255), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)

    status_id = db.Column(db.Integer, ForeignKey('Statuses.id'), nullable=False)
    import src.main.modules.status.status_model
    status = relationship('status_model.Status', backref='tasks')

    priority_id = db.Column(db.Integer, ForeignKey('Priorities.id'), nullable=False)
    import src.main.modules.priority.priority_model
    priority = relationship('priority_model.Priority', backref='tasks')

    project_id = db.Column(db.Integer, ForeignKey('Projects.id'), nullable=False)
    project = relationship('Project', backref='tasks')


    def __repr__(self) -> str:
        return f'<Task: project: {self.project.name} | description: {self.descriptions}>'


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
