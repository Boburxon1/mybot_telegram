import telebot
from keyboards import *  # tugmalar importi

# Sizning bot tokeningiz
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
@bot.message_handler(func=lambda message: message.text in ["5-sinf","6-sinf","7-sinf","8-sinf","9-sinf","10-sinf","11-sinf"])
def sinf_tanlandi(message):
    user_sinf = message.text
    bot.send_message(
        message.chat.id,
        f"✅ {user_sinf} tanlandi.\n\nEndi haftaning kunini tanlang:",
        reply_markup=hafta_kunlari()
    )

# Botni ishga tushirish
bot.polling()
