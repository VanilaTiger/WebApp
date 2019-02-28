import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['aszummer@gmail.com']

    POSTS_PER_PAGE = 3

#---------------------------------------------------------
####The easiest one is to use the SMTP debugging server from Python. This is a fake email server that accepts emails,
# but instead of sending them, it prints them to the console. To run this server, open a second terminal session
# and run the following command on it:
# (venv) $ python -m smtpd -n -c DebuggingServer localhost:8025
# Leave the debugging SMTP server running and go back to your first terminal and
# set MAIL_SERVER=localhost and set MAIL_PORT=8025 in the environment
# Make sure the FLASK_DEBUG variable is set to 0 or not set at all
#----------------------------------------------------------------