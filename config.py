import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('smtp.gmail.com')
    MAIL_PORT = int(os.environ.get("587") or 25)
    MAIL_USE_TLS = os.environ.get("True") is not None
    MAIL_USERNAME = os.environ.get('flaskemailcognibe@gmail.com')
    MAIL_PASSWORD = os.environ.get('Flask1!!!')
    ADMINS = ['flaskemailcognibe@gmail.com']

    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es']

#---------------------------------------------------------
####The easiest one is to use the SMTP debugging server from Python. This is a fake email server that accepts emails,
# but instead of sending them, it prints them to the console. To run this server, open a second terminal session
# and run the following command on it:
# (venv) $ python -m smtpd -n -c DebuggingServer localhost:8025
# Leave the debugging SMTP server running and go back to your first terminal and
# set MAIL_SERVER=localhost and set MAIL_PORT=8025 in the environment
# Make sure the FLASK_DEBUG variable is set to 0 or not set at all
#----------------------------------------------------------------