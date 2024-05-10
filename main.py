import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor

from knopkalarfayli import asosiymenubutton, maxsulotlarbutoon, orqagabutton
api = ''

bot = Bot(api)
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def start(message: Message):
    chatid= message.chat.id
    await bot.send_message(chat_id=chatid, text='Xush kelibsiz', reply_markup=asosiymenubutton())

@dp.message_handler()
async def getcategory(message: Message):
    chatid = message.chat.id
    kategoriya = message.text
    await bot.send_message(chat_id=chatid, text=kategoriya,
                           reply_markup=maxsulotlarbutoon(kategoriya))


@dp.callback_query_handler(lambda call: 'foods' in call.data)
async def getitem(callback: CallbackQuery):
    chatid = callback.message.chat.id
    item = callback.data.split('_')[1]
    print(item)

    database = sqlite3.connect('magazin.sqlite')
    cursor = database.cursor()

    cursor.execute('''SELECT name, about, price, category FROM foods WHERE id = ?''', (item, ))

    maxsulot = cursor.fetchone()
    name = maxsulot[0]
    about = maxsulot[1]
    price = maxsulot[2]
    category = maxsulot[3]
    text = f'Maxsulot nomi: {name}\n\nNarxi: {price}\n\n{about}\n\n{category}'
    await bot.edit_message_text(chat_id=chatid, text=text, message_id=callback.message.message_id, reply_markup=orqagabutton(category))


@dp.callback_query_handler(lambda call: 'orqaga' in call.data)
async def orqaga(callback: CallbackQuery):
    chatid = callback.message.chat.id
    category = callback.data.split('_')[1]
    await bot.edit_message_text(chat_id=chatid, text=category, message_id=callback.message.message_id, reply_markup=maxsulotlarbutoon(category))

executor.start_polling(dp, skip_updates=True)