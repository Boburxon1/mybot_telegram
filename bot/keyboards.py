from telebot import types

def sinf_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        types.KeyboardButton("5-sinf"),
        types.KeyboardButton("6-sinf"),
        types.KeyboardButton("7-sinf"),
    )
    markup.add(
        types.KeyboardButton("8-sinf"),
        types.KeyboardButton("9-sinf"),
        types.KeyboardButton("10-sinf"),
        types.KeyboardButton("11-sinf"),
    )

    return markup
