import telebot
from keyboards import sinf_keyboard, kun_keyboard  # import tugmalari

TOKEN = "import telebot"
from keyboards import sinf_keyboard, kun_keyboard  # tugmalar importi

# 👇 Sizning token
TOKEN = "8534971100:AAH4Gejoq6Nr9aoB1t8gvG7eqJv8LnB_PGw"

bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! 📚\nDars jadvali botiga xush kelibsiz.\n\nSinfingizni tanlang:",
        reply_markup=sinf_keyboard()
    )

# Sinfni tanlaganda hafta kunlarini chiqarish
@bot.message_handler(func=lambda message: "sinf" in message.text)
def sinf_tanlandi(message):
    user_sinf = message.text
    bot.send_message(
        message.chat.id,
        f"✅ {user_sinf} tanlandi.\n\nEndi haftaning kunini tanlang:",
        reply_markup=kun_keyboard()
    )

bot.polling()

bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! 📚\nDars jadvali botiga xush kelibsiz.\n\nSinfingizni tanlang:",
        reply_markup=sinf_keyboard()
    )

# Sinfni tanlaganda hafta kunlarini chiqarish
@bot.message_handler(func=lambda message: "sinf" in message.text)
def sinf_tanlandi(message):
    user_sinf = message.text
    bot.send_message(
        message.chat.id,
        f"✅ {user_sinf} tanlandi.\n\nEndi haftaning kunini tanlang:",
        reply_markup=kun_keyboard()
    )

bot.polling()
