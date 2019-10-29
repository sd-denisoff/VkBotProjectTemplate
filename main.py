from flask import request, json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from config import *
from models import *
from actions import *


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'Hello from server!'


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
    try:
        User.get(User.vk_id == id)
    except User.DoesNotExist:
        User.create(vk_id=id)
        vk.messages.send(user_id=id, random_id=generate_random_id(),
                         message='Возможности 👇', keyboard=get_default_keyboard(id))
    else:
        text_handler(id, data)


def text_handler(id, data):
    if 'payload' in data.keys():
        payload = json.loads(data['payload'])
        action_recognition(id, data, payload)
    else:
        response_generator(id, data)


def action_recognition(id, data, payload):
    if payload['action'] == 'name_of_action':
        pass


def response_generator(id, data):
    vk.messages.send(user_id=id, message='<some default message>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
