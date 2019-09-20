from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
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