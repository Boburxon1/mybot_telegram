from telebot import types

def general_classes():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        types.KeyboardButton("5-sinf"),
        types.KeyboardButton("6-sinf"),
        types.KeyboardButton("7-sinf"),
        types.KeyboardButton("8-sinf")
    )
    markup.row(
        types.KeyboardButton("9-sinf"),
        types.KeyboardButton("10-sinf"),
        types.KeyboardButton("11-sinf")
    )
    return markup

def hafta_kunlari():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        types.KeyboardButton("Dushanba"),
        types.KeyboardButton("Seshanba"),
        types.KeyboardButton("Chorshanba")
    )
    markup.row(
        types.KeyboardButton("Payshanba"),
        types.KeyboardButton("Juma"),
        types.KeyboardButton("Shanba")
    )
<<<<<<< HEAD
    return markup
=======
    return markup
>>>>>>> 0766733cd3e7ed88c79ed18e8ddd91853355d69b
