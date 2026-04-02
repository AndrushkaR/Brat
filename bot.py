import telebot
import random

bot = telebot.TeleBot("8606261670:AAELkQUGM9VCqZus4m9Gt6QKINRabaVbAxE")

@bot.message_handler(func=lambda message: True)  # реагирует на ВСЕ сообщения
def slap_handler(message):
    if message.from_user is None:
        return
    
    user = message.from_user
    name = user.first_name or "кто-то"
    
    # Варианты ответов (можно добавить больше)
    responses = [
        f"👋 Шлёпнул {name}! 😏",
        f"🔥 *Шлёп* по {name}! Не шали!",
        f"🍑 Шлёпнул {name} хорошенько~",
        f"{name}, получай шлёп! 🖐️"
    ]
    
    bot.reply_to(message, random.choice(responses))

print("Бот запущен...")
bot.infinity_polling()
