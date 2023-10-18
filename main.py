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
basket_of_items = []


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    await message.delete()
    await message.answer('Привет! Это бот мерча ТИНТа.\nКакой-то дескрипшн',
                         reply_markup=register_inkb)


@dp.callback_query_handler(text='register')
async def register_call(callback: types.CallbackQuery):
    global id_of_message
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Введите ваши фамилию и имя')
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
                                reply_markup=to_main_menu_inkb)


@dp.callback_query_handler(text='to_main_menu')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.edit_text('Здесь ты можешь выбрать и заказать понравившейся мерч!',
                                     reply_markup=main_menu_inkb)


@dp.callback_query_handler(text='product_list')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.edit_text('Смотри, что у нас есть!\n'
                                     'Нажми, чтобы узнать подробную информацию и добавить в заказ!',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='first_item')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.edit_text('Это футболочка!\nА это её описание)',
                                     reply_markup=first_item_inkb)


@dp.callback_query_handler(text='first_item_s')
async def main_menu_call(callback: types.CallbackQuery):
    basket_of_items.append(("first_item", "S"))
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='first_item_m')
async def main_menu_call(callback: types.CallbackQuery):
    basket_of_items.append(("first_item", "M"))
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='first_item_l')
async def main_menu_call(callback: types.CallbackQuery):
    basket_of_items.append(("first_item", "L"))
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='first_item_xl')
async def main_menu_call(callback: types.CallbackQuery):
    basket_of_items.append(("first_item", "XL"))
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='second_item')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.edit_text('Это шопперик!\nА это его описание)',
                                     reply_markup=second_item_inkb)


@dp.callback_query_handler(text='second_item_add')
async def main_menu_call(callback: types.CallbackQuery):
    basket_of_items.append(("second_item", "-"))
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='third_item')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.edit_text('Это стикерики!\nА это их описание)',
                                     reply_markup=third_item_inkb)


@dp.callback_query_handler(text='third_item_add')
async def main_menu_call(callback: types.CallbackQuery):
    basket_of_items.append(("third_item", "-"))
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
