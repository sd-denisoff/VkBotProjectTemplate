from flask import Flask
import vk_api


APP_URL = ''


CSRF_ENABLED = True
WTF_CSRF_ENABLED = True
SECRET_KEY = '<some_random_string>'

app = Flask(__name__, template_folder='./web/templates', static_folder='./web/static')
app.config.from_object('config')


access_token = '<access_token>'
confirmation_token = '<confirmation_token>'

session = vk_api.VkApi(token=access_token)
vk = session.get_api()
