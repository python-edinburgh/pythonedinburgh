import logging
import re

from django.utils.html import urlize
from google.appengine.api import memcache
from google.appengine.ext import db

from flask import Flask
from flask import render_template
import ical
from jinja2 import Markup
import tweepy

app = Flask(__name__)


class TwitterCredentials(db.Model):
    consumer_key = db.StringProperty(required=True)
    access_token = db.StringProperty(required=True)
    consumer_secret = db.StringProperty(required=True)
    access_secret = db.StringProperty(required=True)


@app.route('/')
def home():
    return render_template('home.html',
            tweets=get_tweets(),
            upcoming_events =ical.upcoming_events());


def twitterfy(tweet):
    # find hashtags
    pattern = re.compile(r"(?P<start>.?)#(?P<hashtag>[A-Za-z0-9_]+)(?P<end>.?)")

    # replace with link to search
    link = r'\g<start>#<a href="http://twitter.com/search?q=\g<hashtag>"  title="#\g<hashtag> search Twitter">\g<hashtag></a>\g<end>'
    text = pattern.sub(link,tweet)

    # find usernames
    pattern = re.compile(r"(?P<start>.?)@(?P<user>[A-Za-z0-9_]+)(?P<end>.?)")

    # replace with link to profile
    link = r'\g<start>@<a href="http://twitter.com/\g<user>"  title="#\g<user> on Twitter">\g<user></a>\g<end>'
    text = pattern.sub(link,text)

    return Markup(urlize(text))


def get_tweets():
    tweets = memcache.get("tweets")

    if tweets is None:
        credentials = TwitterCredentials.all().get()
        if credentials:
            auth = tweepy.OAuthHandler(str(credentials.consumer_key), str(credentials.consumer_secret))
            auth.set_access_token(str(credentials.access_token), str(credentials.access_secret))
            api = tweepy.API(auth_handler=auth)

            # Added for offline development.
            try:
                statuses = api.user_timeline('pythonedinburgh', count=5)
            except tweepy.TweepError:
                logging.exception("Exception obtaining tweets")
                return []

            tweets = [TweetSummary(status) for status in statuses]

            if not memcache.add("tweets", tweets, 60 * 10): # 10 mins.
                logging.error("Memcache tweet store failed.")
        else:
            logging.warning("No Twitter credentials were found in the database. Creating them")
            credentials = TwitterCredentials(consumer_key='a', access_token='a',
                    consumer_secret='a', access_secret='a')
            db.put(credentials)

    return tweets


class TweetSummary(object):
    def __init__(self, tweet):
        self.text = tweet.text

        if hasattr(tweet, 'retweeted_status'):
            self.profile_image_url = tweet.retweeted_status.author.profile_image_url
        else:
            self.profile_image_url = tweet.author.profile_image_url

        self.when = tweet.created_at

    @property
    def html(self):
        return twitterfy(self.text)


app.secret_key = '7%@0g6y!hu^flbmkcfb$@zxs9ftmh=t0blgnog-ibh52za$6nu'
