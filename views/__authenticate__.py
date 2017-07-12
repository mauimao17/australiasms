from flask import Blueprint
from flask import render_template
from flask import request 
from flask import session
from flask import g 

auth = Blueprint('auth',__name__)


auth.route('/google',methods=['GET','POST'])
def googleAuth():
	pass



