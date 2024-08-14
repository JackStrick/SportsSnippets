from config import db

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    short_name = db.Column(db.String(15), unique=False, nullable=True)
    logo = db.Column(db.String(300), unique=False, nullable=True)
    source_link = db.Column(db.String(300), nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "shortName": self.short_name,
            "logo": self.logo,
            "sourceLink": self.source_link,
        }