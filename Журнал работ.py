from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime
from flask import Flask, render_template, url_for


def get_css():
    return url_for('static', filename='css/style.css')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/martians.db')
session = db_session.create_session()


def main():
    app.run()


@app.route('/')
def index():
    param = {
        'jobs': session.query(Jobs).all(),
        'css': get_css()
    }
    return render_template('works_log.html', **param)


if __name__ == '__main__':
    main()
