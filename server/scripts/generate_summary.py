
import os
import requests
import json
from openai import OpenAI
from config import app, db
from dotenv import load_dotenv
from models.topics import Topic
from models.favorited_topics import FavoritedTopic
from models.stories import Story
from models.summaries import Summary

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    organization=os.getenv("OPENAI_ORG"),
    project=os.getenv("OPENAI_PROJECT"),
)

def fetch_headlines(topic):
    url = topic.source_link + '/news'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed - fetch_news - with status code {response.status_code}")

def fetch_story(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed - fetch_news - with status code {response.status_code}")

def summarize(headlines, stories):
    summaries = []
    for headline, story in zip(headlines, stories):
        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a sports writer that summarizes sports news."},
                {"role": "user", "content": f"This is the news headline: {headline}. And this is the article content: {story}. Create a new original article that is a summary of this provided story. Make sure to remove any html. Summaries should be roughly one paragraph in length at minimum and no more than 1500 characters at max"}
            ]
        )
        if (completion.choices[0]):
            summaries.append(completion.choices[0].message.content)
        
        
    return summaries

with app.app_context():
    favorited_topics = FavoritedTopic.query.all()
    
    if favorited_topics:
        # Get only distinct topic Ids
        favorite_ids = {x.get_topic_id() for x in favorited_topics} 
        
        # For each topic:
        #   Fetch recent headlines
        #   Fetch stories from headlines
        #   Generate summary list for each topic
        #   Append summaries to db for topic
        
        for id in favorite_ids:
            topic = db.session.get(Topic, id)
            news = fetch_headlines(topic)
            headlines = []
            stories = []
            web_links = []
            api_links = []
            for article in news['articles']:
                if (article['type'] != 'Media'):
                    story_json = fetch_story(article['links']['api']['news']['href'])
                    headlines.append(article['headline'])
                    web_links.append(article['links']['web']['href'])
                    api_links.append(article['links']['api']['news']['href'])
                    stories.append(story_json['headlines'][0]['story'])

            print("Creating summaries for ", topic.name)        
            summary_list = summarize(headlines, stories)

            if summary_list:
                # Create summary table record
                # Get the newly created id back
                # For each story create story record with data + summary id
                try:
                    summary = Summary(topic_id = topic.id)
                    db.session.add(summary)
                    db.session.flush()
                    
                    for headline, summary_text, web_link, api_link in zip(headlines, summary_list, web_links, api_links):
                        story_obj = Story(
                            summary_id = summary.id,
                            headline = headline,
                            summary = summary_text,
                            web_link = web_link,
                            api_link = api_link
                        )
                        db.session.add(story_obj)
                    
                    db.session.commit()
                    
                except Exception as e:
                    db.session.rollback()
                    print(f"Error Occured: {e}")

            

