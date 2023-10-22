from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputFile, InputMedia, InputMediaPhoto


class MyDialog(StatesGroup):
    answer = State()
    checkout = State()


API_TOKEN = '6368719972:AAFLy5D21ZD-vH4HSjUfHlX1tWnriJtQc_Y'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
id_of_message = 0
basket_of_items = [("third_item", 0), ("second_item", 0)]
current_size = "L"
cost_basket = 0
user_name = "?"


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    await message.delete()
    await message.answer("Привет! Это бот мерча ТИНТа.\nКакой-то дескрипшн", reply_markup=register_inkb)
    #hello_photo = InputFile("system photos/hello_photo.png")
    #await message.answer_photo(InputMediaPhoto("attach://hello_photo.png"), caption="Привет! Это бот мерча ТИНТа.\nКакой-то дескрипшн", reply_markup=register_inkb)


@dp.callback_query_handler(text='register')
async def register_call(callback: types.CallbackQuery):
    global id_of_message
    #register_photo = InputMedia("system photos/register.png")
    #await callback.message.edit_media(register_photo)
    #await callback.message.edit_caption('Введите ваши фамилию и имя')
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Введите ваши фамилию и имя')
    id_of_message = callback.message.message_id
    await MyDialog.answer.set()


@dp.message_handler(state=MyDialog.answer)
async def process_message(message: types.Message, state: FSMContext):
    global user_name, id_of_message
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']

        user_name = user_message
        await MyDialog.answer.set()

    await state.finish()

    # register_db(message.from_user.id, user_message, role_client)

    await bot.delete_message(message.chat.id, id_of_message)
    await message.delete()

    await message.answer('Вы удачно прошли регистрацию',
                         reply_markup=to_main_menu_inkb)


@dp.callback_query_handler(text='to_main_menu')
async def main_menu_call(callback: types.CallbackQuery):
    await callback.message.delete()
    main_photo = InputFile("system photos/main_menu.png")
    await callback.message.answer_photo(main_photo, caption='Здесь ты можешь выбрать и заказать понравившейся мерч!',
                                        reply_markup=main_menu_inkb)
    #await callback.message.edit_text('Здесь ты можешь выбрать и заказать понравившейся мерч!',
    #                                reply_markup=main_menu_inkb)


@dp.callback_query_handler(text='product_list')
async def produc_list(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Смотри, что у нас есть!\n'
                                     'Нажми, чтобы узнать подробную информацию и добавить в заказ!',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='first_item')
async def first_item(callback: types.CallbackQuery):
    await callback.message.delete()
    first_item_photo = InputFile("system photos/first_item.png")
    await callback.message.answer_photo(first_item_photo, caption='Это футболочка!\nА это её описание, осталось лишь выбрать размер.)',
                                        reply_markup=first_item_inkb)


@dp.callback_query_handler(text='first_item_s')
async def first_item_s_size(callback: types.CallbackQuery):
    global current_size
    current_size = "S"
    await callback.message.edit_caption('Добавить в заказ футболочку размером S?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_m')
async def first_item_m_size(callback: types.CallbackQuery):
    global current_size
    current_size = "M"
    await callback.message.edit_caption('Добавить в заказ футболочку размером M?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_l')
async def first_item_l_size(callback: types.CallbackQuery):
    global current_size
    current_size = "L"
    await callback.message.edit_caption('Добавить в заказ футболочку размером L?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_xl')
async def first_item_xl_size(callback: types.CallbackQuery):
    global current_size
    current_size = "XL"
    await callback.message.edit_caption('Добавить в заказ футболочку размером XL?',
                                     reply_markup=first_item_add_inkb)


@dp.callback_query_handler(text='first_item_add')
async def adding_first_item(callback: types.CallbackQuery):
    global cost_basket
    cost_basket += 1300
    basket_of_items.append(("first_item", current_size))
    await callback.message.delete()
    await callback.message.answer('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='second_item')
async def second_item(callback: types.CallbackQuery):
    await callback.message.delete()
    second_item_photo = InputFile("system photos/second_item.png")
    await callback.message.answer_photo(second_item_photo,
                                        caption='Это шопперик!\nА это его описание)',
                                        reply_markup=second_item_inkb)


@dp.callback_query_handler(text='second_item_add')
async def adding_second_item(callback: types.CallbackQuery):
    global cost_basket
    cost_basket += 300
    basket_of_items[1] = (basket_of_items[1][0], basket_of_items[1][1] + 1)
    await callback.message.delete()
    await callback.message.answer('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='third_item')
async def third_item(callback: types.CallbackQuery):
    await callback.message.delete()
    third_item_photo = InputFile("system photos/third_item.png")
    await callback.message.answer_photo(third_item_photo,
                                        caption='Это стикерики!\nА это его описание)',
                                        reply_markup=third_item_inkb)


@dp.callback_query_handler(text='third_item_add')
async def adding_third_item(callback: types.CallbackQuery):
    global cost_basket
    cost_basket += 500
    basket_of_items[0] = (basket_of_items[0][0], basket_of_items[0][1] + 1)
    await callback.message.delete()
    await callback.message.answer('Готово! Айтем добавлен в заказ.\nЧто еще добавим?',
                                     reply_markup=product_list_inkb)


@dp.callback_query_handler(text='basket')
async def basket_call(callback: types.CallbackQuery):
    global cost_basket
    if cost_basket == 0:
        out_answer = "В вашей корзине пока что пусто!"
    else:
        out_answer = "Вот товары, которые находятся в вашей корзине:\n\n"
        for item in basket_of_items:
            if item[0] != "first_item":
                if item[1] != 0:
                    out_answer += item[0] + " " + str(item[1]) + " шт.\n"
            else:
                out_answer += item[0] + " размера " + str(item[1]) + "\n"
        out_answer += "\nОбщая стоимость: " + str(cost_basket) + " рублей."
    await callback.message.delete()
    await callback.message.answer(out_answer,
                                     reply_markup=basket_inkb)


@dp.callback_query_handler(text='clear_basket')
async def clear_basket(callback: types.CallbackQuery):
    basket_of_items.clear()
    global cost_basket
    cost_basket = 0
    try:
        await callback.message.edit_text('В вашей корзине пока что пусто!', reply_markup=basket_inkb)
    except Exception:
        pass


@dp.callback_query_handler(text='checkout')
async def checkout_call(callback: types.CallbackQuery):
    global cost_basket, user_name
    out_answer = ""
    await callback.message.delete()
    if cost_basket == 0:
        await callback.message.answer('В вашей корзине пока что пусто! Вы не можете ничего заказать.',
                                         reply_markup=to_main_menu_inkb)
    else:
        out_answer += "Давай всё проверим!\n"
        out_answer += "Вас зовут " + user_name + "\n\nЗаказ:\n"
        for item in basket_of_items:
            if item[0] != "first_item":
                if item[1] != 0:
                    out_answer += item[0] + " " + str(item[1]) + " шт.\n"
            else:
                out_answer += item[0] + " размера " + str(item[1]) + "\n"

        out_answer += "\nОбщая стоимость: " + str(cost_basket) + " рублей."

        await callback.message.answer(out_answer,
                                         reply_markup=checkout_inkb)


@dp.callback_query_handler(text='final_checkout')
async def final_checkout(callback: types.CallbackQuery):
    global cost_basket
    cost_basket = -1
    await callback.message.delete_reply_markup()
    await callback.message.edit_text("Денюжки переводи вот сюда\n\n +7(952)2812\n\nТвой заказ стоит n руб.\n"
                                     "Обязательно скинь скрин перевода прямо в этот диалог!\nКогда мы все проверим,"
                                     "тебе придет подтверждение. Это может занять до 24 часов")
    # await MyDialog.checkout.set()


@dp.message_handler(content_types=['photo', 'document'])
async def photo_or_doc_handler(message: types.Message):
    global cost_basket
    if cost_basket == -1:
        if message.content_type == 'photo':
            await message.photo[-1].download(destination_file="1.jpg")
        elif message.content_type == 'document':
            await message.document.download(destination_file="1.jpg")
        await message.answer('Всё готов!\n\nОсталось дождаться подтверждения...', )
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
