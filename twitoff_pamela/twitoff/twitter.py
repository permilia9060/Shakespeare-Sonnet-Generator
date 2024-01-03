from os import getenv
import tweepy
from .models import DB, Tweet, User

# get api keys from .env
key = getenv("TWITTER_API_KEY")
secret = getenv("TWITTER_API_KEY_SECRET")
# connect to twitter api
TWITTER_AUTH = tweepy.OAuthHandler(key, secret)
# open access to api
TWITTER = tweepy.API(TWITTER_AUTH)
# add function to communicate with api


def add_or_update_user(username):
        # if user is there pull that user's data and tweets
        # from the api looking for new tweets to add to the db
        # get the user info from twitter
    twitter_user = TWITTER.get_user(screen_name=username)
        # check to see if the user with the same id
        # is already in the db.  If not we will create
        # a new one
    db_user = (User.query.get(twitter_user.id)) or User(id=twitter_user.id)
    # now store in db
    DB.session.add(db_user)

    # get user tweets (in a list)
    tweets = twitter_user.timeline(count=200,
                                   exclude_replies=True,
                                   include_rts=False,
                                   tweet_mode="extended",
                                   since_id=db_user.newest_tweet_id)

    # update the newest_tweet_id if there have been new tweets
    # since the last time this user tweeted
    if tweets:
        db_user.newest_tweet_id = tweets[0].id

    # add tweets one by one to the db
    for tweet in tweets:
        tweet_vector = vectorize_tweet(tweet.full_text)
        db_tweet = Tweet(id=tweet.id,
                        text=tweet.full_text[:300],
                        vect=tweet_vector,
                        user_id=db_user.id)
    DB.session.add(db_tweet)
    # save changes to the db
    DB.session.commit()
