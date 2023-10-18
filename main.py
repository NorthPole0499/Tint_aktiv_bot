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
basket_of_items = [("third_item", 0), ("second_item", 0)]
current_size = "L"
num_of_items = 0


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
    await callback.message.edit_text('Это футболочка!\nА это её описание, осталось лишь выбрать размер.)',
                                     reply_markup=first_item_inkb)


@dp.callback_query_handler(text='first_item_s')
async def main_menu_call(callback: types.CallbackQuery):
    global current_size
    current_size = "S"
    await callback.message.edit_text('Добавить в заказ футболочку размером S?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_m')
async def main_menu_call(callback: types.CallbackQuery):
    global current_size
    current_size = "M"
    await callback.message.edit_text('Добавить в заказ футболочку размером M?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_l')
async def main_menu_call(callback: types.CallbackQuery):
    global current_size
    current_size = "L"
    await callback.message.edit_text('Добавить в заказ футболочку размером L?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_xl')
async def main_menu_call(callback: types.CallbackQuery):
    global current_size
    current_size = "XL"
    await callback.message.edit_text('Добавить в заказ футболочку размером XL?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_add')
async def main_menu_call(callback: types.CallbackQuery):
    global num_of_items
    num_of_items += 1
    basket_of_items.append(("first_item", current_size))
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='second_item')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.edit_text('Это шопперик!\nА это его описание)',
                                     reply_markup=second_item_inkb)


@dp.callback_query_handler(text='second_item_add')
async def main_menu_call(callback: types.CallbackQuery):
    global num_of_items
    num_of_items += 1
    basket_of_items[1] = (basket_of_items[1][0], basket_of_items[1][1] + 1)
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='third_item')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.edit_text('Это стикерики!\nА это их описание)',
                                     reply_markup=third_item_inkb)


@dp.callback_query_handler(text='third_item_add')
async def main_menu_call(callback: types.CallbackQuery):
    global num_of_items
    num_of_items += 1
    basket_of_items[0] = (basket_of_items[0][0], basket_of_items[0][1] + 1)
    await callback.message.edit_text('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='basket')
async def main_menu_call(callback: types.CallbackQuery):
    if num_of_items == 0:
        out_answer = "В вашей корзине пока что пусто!"
    else:
        out_answer = "Вот товары, которые находятся в вашей корзине:\n\n"
        for item in basket_of_items:
            if item[0] != "first_item":
                if item[1] != 0:
                    out_answer += item[0] + " " + str(item[1]) + "шт.\n"
            else:
                out_answer += item[0] + " размера " + str(item[1]) + "\n"

    await callback.message.edit_text(out_answer,
                                     reply_markup=basket_inkb)


@dp.callback_query_handler(text='clear_basket')
async def main_menu_call(callback: types.CallbackQuery):
    basket_of_items.clear()
    global num_of_items
    num_of_items = 0
    try:
        await callback.message.edit_text('В вашей корзине пока что пусто!', reply_markup=basket_inkb)
    except Exception:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
