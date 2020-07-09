from flask import request, json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from config import *
from models import *
from actions import *


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'Hello from bot server!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        user_id = data['object']['from_id']
        user_recognition(str(user_id), data['object'])
    return 'ok'


def user_recognition(id, data):
    if User.query.filter_by(vk_id=id).first() is None:
        user = User(vk_id=id)
        db.session.add(user)
        db.session.commit()
        vk.messages.send(user_id=id, random_id=generate_random_id(),
                         message='Возможности 👇', keyboard=get_default_keyboard(id))
    else:
        message_handler(id, data)


def message_handler(id, data):
    if 'payload' in data.keys():
        payload = json.loads(data['payload'])
        action_recognition(id, data, payload)
    else:
        response_generator(id, data)


def action_recognition(id, data, payload):
    if payload['action'] == 'action_1':
        pass
    elif payload['action'] == 'action_2':
        pass


def response_generator(id, data):
    vk.messages.send(user_id=id, message='')


if __name__ == '__main__':
    application['DOMAIN'] = ''  # fill it
    app.run(host='0.0.0.0', port=5000, debug=True)
