# set up db tables
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# store 2 different kinds of data
class User(DB.Model):
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # username column
    username = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return f"User:  {self.username}"

class Tweet(DB.Model):
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # text column
    text = DB.Column(DB.Unicode(300))
    # user id column (foreign key / secondary key)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False)
    # user column creates a 2-way link between
    # user object and a tweet object
    user = DB.relationship("User", backref=DB.backref("tweets", lazy=True))

    def __repr__(self):
        return f"Tweet:  {self.text}"

    # go to flask repl and make users and tweets using
    # flask shell from outer folder
    # type from twitoff.models import User to import
    # the User class
    # make user   user1 = User(id=1, username="ryan")

    # # type from twitoff.models import Tweet to import
    # the Tweet class
    # tweet1 = Tweet(id=1, text="this is a tweet", user=user1)

    # now connect db to app go to app.py file
