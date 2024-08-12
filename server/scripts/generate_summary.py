import os
from openai import OpenAI

key = os.getenv("OPENAI_APIKEY")

client = OpenAI(
    organization=os.getenv("OPENAI_ORG"),
    project=os.getenv("OPENAI_PROJECT"),
)


article_text = "Blah blah blah"

