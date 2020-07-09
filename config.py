from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_mail import Mail, Message
from threading import Thread
import vk_api
import os


# VK API config

access_token = ''  # fill it
confirmation_token = ''  # fill it

session = vk_api.VkApi(token=access_token)
vk = session.get_api()  # API version: # fill it


# app config

CSRF_ENABLED = True
WTF_CSRF_ENABLED = True
SECRET_KEY = ''  # fill it

application = Flask(__name__, template_folder='./web/templates', static_folder='./web/static')
application.config.from_object('config')

manager = Manager(application)

db = SQLAlchemy(application)
migrate = Migrate(application, db)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(application)
login_manager.login_message_category = 'error'
login_manager.login_message = 'У Вас нет прав для просмотра данной страницы'
login_manager.login_view = ''  # fill it

mail = Mail(application)


def asynchronous(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@asynchronous
def send_async_email(msg):
    with application.app_context():
        mail.send(msg)


def send_email(subject, recipients, html):
    msg = Message(subject, recipients=recipients)
    msg.html = html
    send_async_email(msg)


# email server config

MAIL_SERVER = ''  # fill it
MAIL_PORT = ''  # fill it
MAIL_USE_SSL = True
MAIL_USERNAME = ''  # fill it
MAIL_PASSWORD = ''  # fill it
MAIL_DEFAULT_SENDER = MAIL_USERNAME

# app server config

SERVER_IP = ''  # fill it
SERVER_LOGIN = ''  # fill it
SERVER_PASSWORD = ''  # fill it

# database config

MYSQL_USERNAME = ''  # fill it
MYSQL_PASSWORD = ''  # fill it
MYSQL_PORT = ''  # fill it
MYSQL_DB_NAME = ''  # fill it

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'database.db')  # for development only
