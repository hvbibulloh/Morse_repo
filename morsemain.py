from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from states import ShifrState, Shifrochish, Admin
from morze import to_morse_code, to_english_plain_text
from reply_btn import mainsh, exit_state

PROXY_URL = 'http://proxy.server:3128'
TOKEN = 'YOUR BOT TOKEN 🙂'
bot = Bot(TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def wel(msg: types.message):
    await msg.answer(
        text=f'Assalomu aleykum {msg.from_user.first_name}\nMenga istalgan so\'ni yuboring va men uni "Morse alifbosida shifrlab yuboraman"\n \n Shifrni  ham jo\'natsangiz shifrdan ochib bera olaman!!!',
        reply_markup=mainsh())
    await msg.answer('Bot sinov xolatida ishlayapdi xato kamchiliklar bo\'lsa uzr so\'raymiz 😊 ')


@dp.message_handler(Text("Shifrlash 🔐"))
async def shifr(msg: types.message):
    await ShifrState.comment.set()
    await msg.answer(text='Shifrlash uchun matn (yoki so\'z) kiriting ', reply_markup=exit_state())


@dp.message_handler(state=ShifrState.comment)
async def make_shifr(msg: types.Message, state):
    if msg.text == '❌':
        await state.finish()
        await msg.answer(text='Main Page', reply_markup=mainsh())
    else:
        data = to_morse_code(msg.text)
        await state.finish()
        await msg.reply(text=f"{data}", reply_markup=mainsh())


@dp.message_handler(Text('Shifr ochish 🔓'))
async def shifroch(msg: types.message):
    await Shifrochish.comment.set()
    await msg.answer(text='Shifrlangan matn (yoki so\'z) kiriting', reply_markup=exit_state())


@dp.message_handler(state=Shifrochish.comment)
async def open_shifr(msg: types.Message, state):
    if msg.text == '❌':
        await state.finish()
        await msg.answer(text='Main Page', reply_markup=mainsh())
    else:
        me = to_english_plain_text(msg.text)
        if me:
            await state.finish()
            await msg.reply(text=f" {me.title()}", reply_markup=mainsh())
        else:
            await msg.answer(text="ERROR, xatolik bor 🦦, Shifrlangan matn kiriting 🧠")


@dp.message_handler(Text('Anonim Chat 🙈'))
async def anonim(msg: types.message, state):
    await msg.reply('Hozircha bu yo\'nalish ustida ishlar ketmoqda, tez orada ishga tushadi 😊')


@dp.message_handler(Text('Admin 🦾'))
async def admn(msg: types.Message):
    await Admin.comment.set()
    await msg.answer(text="Aloqadasiz, xabaringiz adminga yetib boradi savol yoki taklifingiz bo\'lsa yuboring 👀: ",
                     reply_markup=exit_state())


@dp.message_handler(state=Admin.comment)
async def admin_state(msg: types.Message, state):
    if msg.text == '❌':
        await msg.answer(text="To'xtatid", reply_markup=mainsh())
        await state.finish()
    else:
        await bot.send_message(941535008,
                               text=f"ID: {msg.from_user.id}\nName: {msg.from_user.first_name}\nUsername: {msg.from_user.username}\nFikrlar: {msg.text}",
                               reply_markup=mainsh())
        await state.finish()


@dp.message_handler(Text('Bizning botlar 🌱'))
async def bots(msg: types.Message):
    await msg.reply(
        text='@secretmorse_bot - Muallif >> @HvbibuLLoh\n@collectJob_bot - Muallif >> @Rozievich\n@kirlat_bot - Muallif >> @Rozievich')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
