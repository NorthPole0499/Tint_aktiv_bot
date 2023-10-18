from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

# register
register_button = InlineKeyboardButton(text='Зарегистрироваться', callback_data='register')
register_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(register_button)

main_menu_button = InlineKeyboardButton(text='Перейти в главное меню', callback_data='to_main_menu')
to_main_menu_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(main_menu_button)

product_list_button = InlineKeyboardButton(text='Список товаров', callback_data='product_list')
basket_button = InlineKeyboardButton(text='Корзина', callback_data='basket')
checkout_button = InlineKeyboardButton(text='Оформить заказ', callback_data='checkout')
main_menu_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(product_list_button,
                                                                               basket_button,
                                                                               checkout_button)

first_item_button = InlineKeyboardButton(text='Первая вещичка', callback_data='first_item')
second_item_button = InlineKeyboardButton(text='Вторая вещичка', callback_data='second_item')
third_item_button = InlineKeyboardButton(text='Третья вещичка', callback_data='third_item')
product_list_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(first_item_button,
                                                                                  second_item_button,
                                                                                  third_item_button,
                                                                                  main_menu_button)

first_item_S_button = InlineKeyboardButton(text='S', callback_data='first_item_s')
first_item_M_button = InlineKeyboardButton(text='M', callback_data='first_item_m')
first_item_L_button = InlineKeyboardButton(text='L', callback_data='first_item_l')
first_item_XL_button = InlineKeyboardButton(text='XL', callback_data='first_item_xl')
first_item_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(first_item_S_button,
                                                                                first_item_M_button,
                                                                                first_item_L_button,
                                                                                first_item_XL_button,
                                                                                product_list_button)

second_item_add_button = InlineKeyboardButton(text='Добавить в корзину', callback_data='second_item_add')
second_item_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(second_item_add_button)

third_item_add_button = InlineKeyboardButton(text='Добавить в корзину', callback_data='third_item_add')
third_item_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(third_item_add_button)




