import sqlite3

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def asosiymenubutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='ichimliklar'),
        KeyboardButton(text='ovqatlar'),
    )

    return markup


def maxsulotlarbutoon(category):
    database = sqlite3.connect('magazin.sqlite')
    cursor = database.cursor()

    cursor.execute('''SELECT name, id FROM foods WHERE category = ?''', (category,))

    maxsulotlar = cursor.fetchall()

    markup = InlineKeyboardMarkup()
    for item in maxsulotlar:
        markup.add(
            InlineKeyboardButton(text=item[0], callback_data=f'foods_{item[1]}')
        )

    return markup


def orqagabutton(category):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text='Orqaga', callback_data=f'orqaga_{category}')
    )


    return markup
