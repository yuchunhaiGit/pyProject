from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import abort
from flask_script import Manager
from datetime import datetime
from flask_moment import Moment
from flask_bootstrap import Bootstrap
import templates


app = Flask(__name__)
moment = Moment(app)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/t1')
def t1():
    return 'Hello World!'

@app.route('/t2/<name>')
def t2(name):
    return 'Hello World!,%s' %name

@app.route('/t3')
def t3():
    user_ganet = request.headers.get('User-Agent')
    return 'your browser is %s'%user_ganet

@app.route('/t4')
def t4():
    return 'Bad Request',400

@app.route('/t5')
def t5():
    response = make_response('cookie')
    response.set_cookie('answer','42')
    return response

@app.route('/t6')
def t6():
    return redirect('https://www.baidu.com')

# @app.route('/t7/<id>')
# def t7(id):
#     # user = load_user(id)
#     user = __loader__(id)
#     if not user:
#         abort(404)
#     return 'Hello,%s' %user.name

@app.route('/t7')
def t7():
    return render_template('index.html',current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run()
    # manager.run()