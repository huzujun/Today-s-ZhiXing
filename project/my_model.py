from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    nick_name = db.Column(db.String(50))
    profile = db.Column(db.String(100))
    intro = db.Column(db.Text)
    circle1 = db.Column(db.Integer)
    circle2 = db.Column(db.Integer)
    circle3 = db.Column(db.Integer)
    circle4 = db.Column(db.Integer)
    circle5 = db.Column(db.Integer)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def update(self, nick_name, intro, profile, circle1, circle2, circle3, circle4, circle5):
        self.nick_name = nick_name
        self.intro = intro
        self.profile = profile
        self.circle1 = circle1
        self.circle2 = circle2
        self.circle3 = circle3
        self.circle4 = circle4
        self.circle5 = circle5


class UserSchema(ma.Schema):
    user_id = fields.Integer()
    username = fields.String()
    password = fields.String()
    email = fields.Email()
    studentID = fields.Integer()
    intro = fields.String()
    nick_name = fields.String()
    profile = fields.String()
    circle1 = fields.Integer()
    circle2 = fields.Integer()
    circle3 = fields.Integer()
    circle4 = fields.Integer()
    circle5 = fields.Integer()


class Circle(db.Model):
    __tablename__ = 'circle'
    circle_id = db.Column(db.Integer, primary_key=True)
    circle_name = db.Column(db.String(20), unique=True)
    people_number = db.Column(db.Integer)

    def __init__(self, circle_name, people_number):
        self.circle_name = circle_name
        self.people_number = people_number


class CircleSchema(ma.Schema):
    circle_id = fields.Integer()
    circle_name = fields.String()
    people_number = fields.Integer()


class Post(db.Model):
    __tablename__ = 'post'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    circle_id = db.Column(db.Integer, db.ForeignKey('circle.circle_id'))
    postTime = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    contend = db.Column(db.String(100))
    img = db.Column(db.String(100))
    likes = db.Column(db.Integer)
    favorites = db.Column(db.Integer)

    def __init__(self, user_id, circle_id, contend, img):
        self.user_id = user_id
        self.circle_id = circle_id
        self.contend = contend
        self.img = img


class PostSchema(ma.Schema):
    post_id = fields.Integer()
    user_id = fields.Integer()
    circle_id = fields.Integer()
    contend = fields.String()
    img = fields.String()
    likes = fields.Integer()
    favorites = fields.Integer()


'''
class Comments(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    commentTime = db.Column(db.DateTime)
    contend = db.Column(db.Text)
    likes = db.Column(db.Integer)


class Favorites(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    favouriteTime = db.Column(db.DateTime)


class Likes(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    likeTime = db.Column(db.DateTime)


class Block(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)


class Report(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    reason = db.Column(db.Text)


class CreateCircle(db.Model):
    circle_id = db.Column(db.Integer, primary_key=True)
    circleName = db.Column(db.String(20))
    applyNumber = db.Column(db.Integer)
'''
