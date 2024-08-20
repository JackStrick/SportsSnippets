from config import db

class FavoritedTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    topic_id = db.Column(db.Integer, unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "topicId": self.topic_id,
        }
    
    def get_topic_id(self):
        return self.topic_id