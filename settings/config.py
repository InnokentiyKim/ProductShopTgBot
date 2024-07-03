import os
from emoji import emojize

TOKEN = ''
DB_NAME = 'products.sql'
VERSION = '1.0.0'
AUTHOR = 'InnCent'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATABASE = os.path.join('postgresql://' + BASE_DIR, DB_NAME)
DATABASE = os.path.join(BASE_DIR, DB_NAME)
COUNT = 0

KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(":speech_baloon: О Магазине"),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOWN': emojize('🔽'),
    'UP': emojize('🔼'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'APPLY': emojize('✅ Оформить заказ'),
    'COPY': emojize('©️')
}

CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3
}

COMMANDS = {
    'START': "start",
    'HELP': "help"
}
