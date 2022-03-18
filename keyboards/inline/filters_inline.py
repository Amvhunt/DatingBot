from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def filters_keyboard():
    markup = InlineKeyboardMarkup(row_width=3)
    search_name = InlineKeyboardButton(text="Поиск по имени", callback_data="search_by_name")
    search_age = InlineKeyboardButton(text="Поиск по возрасту", callback_data="search_by_age")
    search_city = InlineKeyboardButton(text="Поиск по городу", callback_data="search_by_city")
    search_gender = InlineKeyboardButton(text="Поиск по полу", callback_data="search_by_gender")
    search_nationality = InlineKeyboardButton(text="Поиск по национальности", callback_data="search_nationality")
    back_to_menu = InlineKeyboardButton(text="⏪️ Вернуться в меню", callback_data="start_menu")
    markup.row(search_name, search_age)
    markup.add(search_city)
    markup.row(search_gender, search_nationality)
    markup.add(back_to_menu)
    return markup
