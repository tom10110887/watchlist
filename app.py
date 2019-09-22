from flask import url_for
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click

WIN = sys.platform.startswith('win')
if WIN: #如果是windows系统，使用三个斜杠
    prefix = 'sqlite:///'
else: #否则，使用四个斜杠
    prefix = 'sqlite:////'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #关闭对模型修改的监控
db = SQLAlchemy(app)

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database"""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.cli.command()
def forge():
    """Generate fake data"""
    db.create_all()

    name = 'Tom Wang'
    movies = [
        {'title': '低俗小说', 'year': '1994'},
        {'title': '这个男人来自地球', 'year': '2007'},
        {'title': '现代爱情故事', 'year': '1991'},
        {'title': '内布拉斯加', 'year': '2013'},
        {'title': '无姓之人', 'year': '2009'},
        {'title': '午夜巴黎', 'year': '2011'},
        {'title': '她', 'year': '2013'},
        {'title': '当哈利遇上莎莉', 'year': '1989'},
        {'title': '云图', 'year': '2012'},
        {'title': 'V字仇杀队', 'year': '2005'}
        ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done.')

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)

@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html'), 404
