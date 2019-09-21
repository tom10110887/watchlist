from flask import url_for
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def hello():
    return u'欢迎来到我的 watchlist!'

@app.route('/t')
def totoro():
    return '<h1>Hello Totoro!</h1><img src="https://n.sinaimg.cn/tech/transform/454/w231h223/20190917/94ce-ietnfsp9713302.gif">'

@app.route('/user/<name>')
def user_page(name):
    return 'user: %s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('totoro'))
    print(url_for('user_page', name='tom'))
    print(url_for('user_page', name='cici'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test page'

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

name = "Tom Wang"
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
