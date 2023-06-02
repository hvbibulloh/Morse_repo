from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def mainsh():
    icon = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    icon.add(KeyboardButton('Shifrlash 🔐'), KeyboardButton('Shifr ochish 🔓'), KeyboardButton('Anonim Chat 🙈'),
             KeyboardButton('Admin 🦾'), KeyboardButton('Bizning botlar 🌱'))
    return icon


def exit_state():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn.add(KeyboardButton('❌'))
    return btn
