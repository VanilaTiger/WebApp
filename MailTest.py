from flask_mail import Message
from app import mail, app
import os

MAIL_SERVER = os.environ.get('smtp.gmail.com')
MAIL_PORT = int(os.environ.get("587") or 25)
MAIL_USE_TLS = os.environ.get("True") is not None
MAIL_USERNAME = os.environ.get('flaskemailcognibe@gmail.com')
MAIL_PASSWORD = os.environ.get('Flask1!!!')
ADMINS = ['flaskemailcognibe@gmail.com']

msg = Message('test subject', sender=app.config['ADMINS'][0],
recipients=['flaskemailcognibe@gmail.com'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)

#Flask1!!!
#flaskemailcognibe@gmail.com