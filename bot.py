from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
from app.signal_generator import generate_signal

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("👋 Welcome! Type /signal to get crypto trade advice.")

def signal(update, context):
    update.message.reply_text("⏳ Analyzing market, please wait...")
    result = generate_signal()
    update.message.reply_text(result)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signal", signal))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
