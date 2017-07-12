


class Config(object):
	DEBUG = True
	DEVELOPMENT = True 
	SECRET_KEY = '@!secretkey!'
	static_folder = 'static'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://super:!important@inqw-442.postgres.pythonanywhere-services.com:10442/sms'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class Auth(object):
	CLIENT_ID = ('KEY')
	CLIENT_SECRET = 'SECRET'
	REDIRECT_URI = 'https://localhost:5000/authorize/google'
	AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
	TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
	USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
