# ###################
from flask import Flask, render_template, request
from .models import DB, User, Tweet
from .twitter import add_or_update_user

DB = SQLAlchemy()

app = Flask(__name__)



    @app.route("/")
    def root():
        users = User.query.all()
        return render_template("base.html", title="Home", users=users)
    # ###################

    # got to terminal and export FLASK_APP= app shows where
    # this app lives in inner folder then flask run
    # close then restart (cntrl c, flask run)
    # refresh app page


# add html go to terminal inner folder mkdir
# templates, them make file base.html
# put in html file
# cd .. to twitoff, flask run, import render_template
# to let Flask use html template
# return render_template("base.html")
# close server, restart, refresh

# next we want to start from outer folder use factory
# use create app def create_app highlight all, tab

# go to init.py

# Coming back from flask shell make 2 new routes

    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("base.html", title="Reset Database")
    # drop all db tables

    @app.route("/populate")
    def populate():
        add_or_update_users("austin")
        add_or_update_users("nasa")
        add_or_update_users("ryanallred")

        return render_template("base.html", title="Populate Database")

    @app.route("/update")
    def update():
        # get list of usernames of all users
        users = User.query.all()

        for username in [user.username for user in users]:
            add_or_update_user(username)

        return render_template("base.html", title="Users Updated")

    @app.route("/user",methods=["POST"])
    @app.route("/user/<username>", methods=["GET"])
    def user(username=None,message=""):

    usrname = username=None or request.values["user_name"]



    return app
