
import os
from openai import OpenAI
from config import app, db, bcrypt
from dotenv import load_dotenv
from models.topics import Topic
from models.favorited_topics import FavoritedTopic

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    organization=os.getenv("OPENAI_ORG"),
    project=os.getenv("OPENAI_PROJECT"),
)


with app.app_context():
    favorited_topics = FavoritedTopic.query.all()
    
    mapped_topics = list(map(lambda x: x.to_json(), favorited_topics))
    print(mapped_topics[0])


article_text = "Blah blah blah"

