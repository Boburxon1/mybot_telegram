import telebot
from keyboards import general_classes, hafta_kunlari

TOKEN = "8534971100:AAH4Gejoq6Nr9aoB1t8gvG7eqJv8LnB_PGw"  # <-- O'zing tokenni shu yerga qo'yasan
bot = telebot.TeleBot(TOKEN)

user_data = {}

# 9-sinf dars jadvali
jadval_9 = {
    "Dushanba": "📘 Algebra\n📖 Adabiyot\n🌍 Tarix",
    "Seshanba": "📗 Ingliz tili\n🧪 Biologiya",
    "Chorshanba": "📘 Geometriya\n🧪 Fizika",
    "Payshanba": "📖 Ona tili\n🌍 Geografiya",
    "Juma": "📗 Ingliz tili\n⚽ Jismoniy tarbiya",
    "Shanba": "📘 Algebra"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! 📚\nMaktab dars jadvali botiga xush kelibsiz.\n\nSinfingizni tanlang:",
        reply_markup=general_classes()
    )

@bot.message_handler(func=lambda m: m.text.endswith("-sinf"))
def sinf_tanlandi(message):
    if message.text != "9-sinf":
        bot.send_message(
            message.chat.id,
            "⛔ Hozircha faqat 9-sinf uchun jadval mavjud."
        )
        return

    user_data[message.chat.id] = "9-sinf"
    bot.send_message(
        message.chat.id,
        "✅ 9-sinf tanlandi.\n\n📅 Haftaning kunini tanlang:",
        reply_markup=hafta_kunlari()
    )

@bot.message_handler(func=lambda m: m.text in [
    "Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba"
])
def kun_tanlandi(message):
    if user_data.get(message.chat.id) != "9-sinf":
        bot.send_message(message.chat.id, "❗ Avval 9-sinfni tanlang.")
        return

    darslar = jadval_9.get(
        message.text,
        "❌ Bu kunga jadval yo‘q."
    )

    bot.send_message(
        message.chat.id,
        f"📚 9-sinf\n📅 {message.text}\n\n{darslar}"
    )

bot.polling()
