"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from openaq import OpenAQ
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"


DB = SQLAlchemy(app)
api = OpenAQ()


def get_results():

    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    results = body["results"]
    tuples_list = []
    for result in results:
        date = result["date"]["utc"]
        value = result["value"]
        tuples_list.append((date, value))
    return tuples_list


class Record(DB.Model):
    '''record class'''
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(200))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'time: {self.datetime}, air quality: {self.value}'


@app.route('/')
def root():
    return str(Record.query.filter(Record.value >= 18).all())


@app.route('/refresh')
def refresh():
    DB.drop_all()
    DB.create_all()
    for item in get_results():
        date = item[0]
        value = item[1]
        record = Record(datetime=date, value=value)
        DB.session.add(record)
    DB.session.commit()
    return 'Data refreshed!'
