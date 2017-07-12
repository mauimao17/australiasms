from flask import Flask
from flask import request 
from flask import render_template 
from flask import redirect 
from flask import url_for
from flask import session 
from flask import g
from views.__api__ import api
from views.__authenticate__ import auth

app = Flask(__name__)
app.config.from_object('config.Config')

app.register_blueprint(api, url_prefix='/api/v1')
app.register_blueprint(auth, url_prefix='/authorize')

@app.before_request
def prepareRequest():
	session.update(user=None)

@app.route('/')
def index():
	return render_template('index.html')

#--------------------
@app.errorhandler(404)
def pageNotFound(e):
	return "Sorry, but the page you requested was not found", 404
#--------------------
@app.errorhandler(500)
def internalError(e):
	return "Sorry, but we're currently fucked up", 500

if __name__ == '__main__':
	app.run()
