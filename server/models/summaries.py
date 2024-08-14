from config import db
from datetime import datetime

class Summary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.String(100), unique=False, nullable=False)
    summary = db.Column(db.String(300), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_json(self):
        return {
            "id": self.id,
            "topicId": self.topic_id,
            "summary": self.summary,
            "datePosted": self.date_posted,
        }