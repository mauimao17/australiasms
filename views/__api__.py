from flask import Blueprint
from flask import render_template
from flask import request 
from flask import session
from flask import g 


api = Blueprint('api',__name__)


@api.route('/user')
def user():
	return 'test'
