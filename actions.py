from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import string
import random

from models import *


def generate_random_id():
    random_id = int(''.join(random.choice(string.digits) for _ in range(10)))
    return random_id


def get_default_keyboard(id):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(label='Button 1', color=VkKeyboardColor.PRIMARY, payload={'action': 'action_1'})
    keyboard.add_line()
    keyboard.add_button(label='Button 2', color=VkKeyboardColor.PRIMARY, payload={'action': 'action_2'})

    if User.query.filter_by(vk_id=id).first().role == 'admin':
        pass

    default_keyboard = keyboard.get_keyboard()
    return default_keyboard
