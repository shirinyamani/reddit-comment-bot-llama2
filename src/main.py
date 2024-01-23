import praw
import os
from utils import call_llama
import time
import requests
from constants import *


#SET USER AGENT
url = "https://www.reddit.com/api/v1/me"
# Set your user agent in the headers
headers = {
    'User-Agent': 'YOUR_REDDIT_APP_NAME/1.0 by YOUY_REDDIT_USERNAME'}
# Make a request to the Reddit API
response = requests.get(url, headers=headers)


def reddit_bot(sub, trigger_phrase, comment_limit=10):
    reddit = praw.Reddit(
        client_id=os.environ['client_id'],
        client_secret=os.environ['client_secret'],
        username=os.environ['username'],
        password=os.environ['passwordred'],
        user_agent=os.environ['user_agent']
    )

    subreddit = reddit.subreddit(sub)

    for comment in subreddit.comments(limit=comment_limit):
        if trigger_phrase in comment.body.lower():
            prompt = comment.body.strip()
            print(f"Processing comment: {comment.id}, body: {comment.body}")
            print(f"Trigger phrase found. Prompt: /n {prompt}")

            # Call Llama 2 API
            similar_words = call_llama(prompt= prompt, model='llama2', stream=False)

            if similar_words:
                reply_text = ' '.join(similar_words)
                print(f"Reply text: {reply_text}")
                comment.reply(reply_text)
                time.sleep(2)  # Add a delay between comments to avoid rate limiting
            else:
                print("Llama 2 API did not provide suggestions for the given prompt.")


if __name__ == '__main__':
    reddit_bot(sub='python', trigger_phrase='sql', comment_limit=15)

