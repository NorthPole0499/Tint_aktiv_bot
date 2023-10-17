from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

#register
register_button = InlineKeyboardButton(text='Зарегистрироваться', callback_data='register')
register_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(register_button)

main_menu_button = InlineKeyboardButton(text='Заказать товар', callback_data='to_main_menu')
to_main_menu_admin_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(main_menu_button)
