from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from settings import config
from data_base.dbalchemy import DBManager


class Keyboards:

    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_button(self, name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item_button_1 = self.set_button('CHOOSE_GOODS')
        item_button_2 = self.set_button('INFO')
        item_button_3 = self.set_button('SETTINGS')
        self.markup.row(item_button_1)
        self.markup.row(item_button_2, item_button_3)
        return self.markup


