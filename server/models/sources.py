from config import db

class Sources(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    link = db.Column(db.String(300), unique=False, nullable=False)
    end_point = db.Column(db.Integer, unique=False, nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link,
            "endPoint": self.end_point,
        }