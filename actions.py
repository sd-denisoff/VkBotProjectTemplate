from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from models import *

import string
import random


def generate_random_id():
    random_id = int(''.join(random.choice(string.digits) for _ in range(10)))
    return random_id


def get_default_keyboard(id):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(label='Button 1', color=VkKeyboardColor.PRIMARY, payload={'action': 'name_of_action_1'})
    keyboard.add_line()
    keyboard.add_button(label='Button 2', color=VkKeyboardColor.PRIMARY, payload={'action': 'name_of_action_2'})

    if User.get(User.vk_id == id).role == 'admin':
        pass

    default_keyboard = keyboard.get_keyboard()
    return default_keyboard
