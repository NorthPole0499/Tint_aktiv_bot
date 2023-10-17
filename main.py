from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class MyDialog(StatesGroup):
    answer = State()


API_TOKEN = '6368719972:AAFLy5D21ZD-vH4HSjUfHlX1tWnriJtQc_Y'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
id_of_message = 0


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    await message.delete()
    await message.answer('Привет! Это тг бот ТИНТа. Чтобы начать позьзоваться им, пройди регистрацию.',
                         reply_markup=register_inkb)


@dp.callback_query_handler(text='register')
async def register_call(callback: types.CallbackQuery):
    global id_of_message
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Введите ваши ФИО')
    id_of_message = callback.message.message_id
    await MyDialog.answer.set()


@dp.message_handler(state=MyDialog.answer)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']

        await MyDialog.answer.set()

    await state.finish()

    #register_db(message.from_user.id, user_message, role_client)

    await bot.delete_message(message.chat.id, id_of_message)
    await message.delete()

    await message.answer('Вы удачно прошли регистрацию',
                                reply_markup=to_main_menu_admin_inkb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
