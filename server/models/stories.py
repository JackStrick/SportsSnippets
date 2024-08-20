from config import db

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary_id = db.Column(db.Integer, unique=False, nullable=False)
    headline = db.Column(db.String(300), unique=False, nullable=False)
    summary =  db.Column(db.String(1500), unique=False, nullable=False)
    web_link = db.Column(db.String(300), unique=False, nullable=False)
    api_link = db.Column(db.String(300), unique=False, nullable=True)
   


    def to_json(self):
        return {
            "id": self.id,
            "summaryId": self.summary_id,
            "headline": self.headline,
            "summary": self.summary,
            "webLink": self.web_link,
            "apiLink": self.api_link,
        }