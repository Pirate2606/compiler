from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy()


class Practice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem_title = db.Column(db.String(256))
    problem_desc = db.Column(db.String(256))
    problem_link = db.Column(db.String(256))
    problem_site = db.Column(db.String(256))
    problem_diff = db.Column(db.String(256))


class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contest_name = db.Column(db.String(256))
    contest_link = db.Column(db.String(256))
    contest_status = db.Column(db.String(256))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    profile_pic = db.Column(db.String(256))


class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)


# setup login manager
login_manager = LoginManager()
login_manager.login_view = "google.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
