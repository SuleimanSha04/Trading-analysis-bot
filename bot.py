import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello! 👋 Your bot is working.")

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "I received your message!")

print("Bot is running...")
bot.infinity_polling()
