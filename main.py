from flask import Flask, render_template, redirect, Blueprint, jsonify, abort
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.users import User
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs)
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init("db/main.sqlite")
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')


if __name__ == '__main__':
    main()
