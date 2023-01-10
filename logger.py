from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime as dt


def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE, result):
    time = dt.now().strftime('%H:%M')
    file = open('db.csv', 'a')
    file.write(f'{time}, {update.effective_user.first_name},{update.effective_user.id}, {update.message.text} = {result}\n')
    file.close()
